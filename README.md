# ISAC_destructive_testing_rigorously_usecases
To ensure the ultimate reliability, security, and safety boundaries of network-based environmental sensing by intentionally stress-testing and corrupting the system.

## Offline laboratory harness

`isac_lab.py` is a dependency-free Python 3.10+ **simulation**, not a radio,
Ericsson product integration, or certification of a live network. It opens no
sockets, emits no RF, accepts no network targets, and performs no hardware actions.
All fault injection is against synthetic in-process state.

From the repository root:

```sh
python isac_lab.py --scenario all --seed 42
python -m unittest -v test_isac_lab
```

The CLI prints JSON with the configuration, scenario metrics, explicit violations,
and a `passed` flag. Exit codes: **0** all checks passed, **1** a quality/safety
limit failed, **2** invalid arguments. Repeat a configuration and seed to reproduce
the results. No third-party dependencies, build step, or linter are required.

| Scenario | Injected fault and checks |
| --- | --- |
| `baseline` | Four synchronized nodes observing a synthetic moving 3D target. |
| `communication` | Excess sensing demand; reserve voice/data capacity first and shed sensing work. |
| `node_dropout` | Remove one tower; require three distinct nodes for fusion. |
| `clock_failure` | Desynchronize one tower; reject its observations and continue on the other three. |
| `signal_corruption` | Inject malformed pulse-Doppler samples, non-finite values, distant ghosts and multipath-like outliers; check rejection and tracking error. |
| `edge_overload` | Saturate a bounded logical work queue; report dropped sensing work and peak queue occupancy. |
| `sabotage` | Combine overload, corrupt observations and a complete temporary tower blackout; coast for at most three steps, then report tracking loss. |

Faults begin at step 3 (zero-based) and last `--fault-duration` steps. Defaults
exercise recovery within the modeled redundancy/coasting budget. Explore the
breaking point with, for example:

```sh
python isac_lab.py --scenario sabotage --fault-duration 5
```

This deliberately returns **1** with `tracking continuity lost`. Use
`--max-tracking-error` to set the 3D error limit (default 2 simulation distance
units), `--sensing-load` for offered work units per step, and `--steps` for duration.
Steps (8–10,000), load (1–1,000,000) and fault duration (1 through steps minus 4)
are validated and bounded. Load is counted arithmetically rather than allocated
as large payloads, keeping memory and execution bounded.

### Model and limitations

Each step reserves 10 voice and 50 data units out of 100 radio units. Sensing
uses only the remainder and a separate queue of 64 units, serviced at 16 units
per step. These abstract reservations illustrate isolation; they do not measure
latency, throughput, RF coexistence, or a real scheduler. Communication drops,
tracking loss, and maximum Euclidean tracking error determine pass/fail.

Observations are already synthetic Cartesian positions, not raw RF/IQ data.
Fusion averages at least three valid, distinct tower observations; a
constant-velocity predictor bridges up to three missing updates. Samples must
be finite, within Doppler/clock limits, and within a spatial gate of the
prediction. These gates are not authentication and cannot detect every plausible
spoof. The harness is not an AI detector, physical multi-static radar model,
real API load generator, memory-leak detector, or security vulnerability scanner.

Real rollout evidence still requires an authorized isolated testbed, actual
scheduler/fusion/AI/API integrations, calibrated traces and ground truth,
latency and accuracy SLOs, resource instrumentation, rollback/interlock procedures,
and independent security assessment. Passing this simulation must never be
treated as proof that destructive tests are safe on an operator network.
