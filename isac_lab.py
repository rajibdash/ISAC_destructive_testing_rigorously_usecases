"""Bounded, offline ISAC fault simulation; never connects to network equipment."""

import argparse
from dataclasses import asdict, dataclass
import json
import math
import random

# These are basic scenarios
SCENARIOS = (
    "baseline",
    "communication",
    "node_dropout",
    "clock_failure",
    "signal_corruption",
    "edge_overload",
    "sabotage",
)


@dataclass(frozen=True)
class Config:
    steps: int = 40
    seed: int = 0
    fault_duration: int = 2
    sensing_load: int = 500
    max_tracking_error: float = 2.0

    def __post_init__(self):
        for name, low, high in (
            ("steps", 8, 10000),
            ("seed", 0, 2**32 - 1),
            ("fault_duration", 1, self.steps - 4),
            ("sensing_load", 1, 1000000),
        ):
            value = getattr(self, name)
            if type(value) is not int or not low <= value <= high:
                raise ValueError(f"{name} must be an integer in [{low}, {high}]")
        if (
            isinstance(self.max_tracking_error, bool)
            or not isinstance(self.max_tracking_error, (float, int))
            or not math.isfinite(self.max_tracking_error)
            or self.max_tracking_error < 0
        ):
            raise ValueError("max_tracking_error must be finite and nonnegative")


@dataclass(frozen=True)
class Observation:
    node: int
    position: object
    doppler: object
    clock_error_ns: float = 0.0


def valid_observation(observation, predicted):
    """Reject malformed samples, unsynchronized nodes and spatial outliers."""
    position = observation.position
    return (
        type(observation.node) is int
        and 0 <= observation.node < 4
        and isinstance(position, (tuple, list))
        and len(position) == 3
        and all(
            type(value) in (float, int) and math.isfinite(value)
            for value in (*position, observation.doppler, observation.clock_error_ns)
        )
        and abs(observation.clock_error_ns) <= 100
        and abs(observation.doppler) <= 100
        and (predicted is None or math.dist(position, predicted) <= 5)
    )


def fuse(observations, predicted):
    positions = {}
    rejected = 0
    for observation in observations:
        if not valid_observation(observation, predicted) or observation.node in positions:
            rejected += 1
            continue
        positions[observation.node] = observation.position
    if len(positions) < 3:
        return None, rejected
    return tuple(
        sum(position[axis] for position in positions.values()) / len(positions)
        for axis in range(3)
    ), rejected


def run_scenario(name, config=None):
    if name not in SCENARIOS:
        raise ValueError(f"unknown scenario: {name}")
    config = config if config is not None else Config()
    rng = random.Random(config.seed)
    queue_capacity = 64
    processing_budget = 16
    queue = peak_queue = sensing_dropped = rejected = lost = coasted = 0
    communication_dropped = 0
    max_error = 0.0
    position = None
    velocity = (0.0, 0.0, 0.0)
    missed = 0

    for step in range(config.steps):
        # Abstract radio units: reserve voice and data before admitting sensing.
        voice, data, capacity = 10, 50, 100
        communication_dropped += max(0, voice + data - capacity)
        fault_active = 3 <= step < 3 + config.fault_duration
        requested = config.sensing_load if fault_active and name in (
            "communication", "edge_overload", "sabotage"
        ) else 8
        admitted = min(requested, capacity - voice - data)
        sensing_dropped += requested - admitted
        available = queue_capacity - queue
        queue += min(admitted, available)
        sensing_dropped += max(0, admitted - available)
        peak_queue = max(peak_queue, queue)
        processed = min(queue, processing_budget)
        queue -= processed

        truth = (float(step), step * 0.5, 100 + step * 0.25)
        predicted = None if position is None else tuple(
            position[axis] + velocity[axis] for axis in range(3)
        )
        observations = []
        for node in range(4):
            if fault_active and (
                (name == "node_dropout" and node == 0) or name == "sabotage"
            ):
                continue
            measured = tuple(value + rng.uniform(-0.02, 0.02) for value in truth)
            clock_error = 1000 if (
                fault_active and name == "clock_failure" and node == 0
            ) else 0
            observations.append(Observation(node, measured, 1.0, clock_error))
        if fault_active and name in ("signal_corruption", "sabotage"):
            observations = [
                Observation(0, (float("nan"), 0, 0), 1),
                Observation(1, ("malformed",), None),
                Observation(2, tuple(value + 100 for value in truth), 1),
                Observation(3, tuple(value + 20 for value in truth), float("inf")),
                Observation(0, tuple(value + 50 for value in truth), 1),
            ] + observations
        measured, invalid = fuse(observations if processed >= 4 else [], predicted)
        rejected += invalid
        if measured is not None:
            if position is not None:
                velocity = tuple(
                    measured[axis] - position[axis] for axis in range(3)
                )
            position = measured
            missed = 0
        else:
            missed += 1
            position = predicted
            if position is None or missed > 3:
                lost += 1
            else:
                coasted += 1
        if position is not None:
            max_error = max(max_error, math.dist(position, truth))

    violations = []
    if communication_dropped:
        violations.append("communication traffic dropped")
    if lost:
        violations.append("tracking continuity lost")
    if max_error > config.max_tracking_error:
        violations.append("tracking error exceeded limit")
    return {
        "scenario": name,
        "config": asdict(config),
        "passed": not violations,
        "violations": violations,
        "metrics": {
            "communication_dropped": communication_dropped,
            "sensing_dropped": sensing_dropped,
            "peak_queue": peak_queue,
            "queue_capacity": queue_capacity,
            "final_queue": queue,
            "rejected_observations": rejected,
            "coasted_steps": coasted,
            "lost_steps": lost,
            "max_tracking_error": max_error,
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=("all", *SCENARIOS), default="all")
    parser.add_argument("--steps", type=int, default=40)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--fault-duration", type=int, default=2)
    parser.add_argument("--sensing-load", type=int, default=500)
    parser.add_argument("--max-tracking-error", type=float, default=2.0)
    args = parser.parse_args(argv)
    try:
        config = Config(
            args.steps, args.seed, args.fault_duration,
            args.sensing_load, args.max_tracking_error,
        )
    except ValueError as error:
        parser.error(str(error))
    names = SCENARIOS if args.scenario == "all" else (args.scenario,)
    results = [run_scenario(name, config) for name in names]
    print(json.dumps({"lab_only": True, "results": results}, indent=2, allow_nan=False))
    return 0 if all(result["passed"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
