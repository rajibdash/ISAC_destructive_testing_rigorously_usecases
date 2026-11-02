import contextlib
import io
import json
import unittest

from isac_lab import Config, Observation, SCENARIOS, fuse, main, run_scenario


class LabTests(unittest.TestCase):
    def test_default_scenarios_pass_and_are_reproducible(self):
        for name in SCENARIOS:
            with self.subTest(scenario=name):
                result = run_scenario(name)
                self.assertTrue(result["passed"], result)
                self.assertEqual(result, run_scenario(name))
                self.assertEqual(result["metrics"]["communication_dropped"], 0)

    def test_overload_is_bounded_and_sheds_only_sensing(self):
        for name in ("communication", "edge_overload", "sabotage"):
            result = run_scenario(name, Config(sensing_load=1000000))
            metrics = result["metrics"]
            self.assertTrue(result["passed"])
            self.assertGreater(metrics["sensing_dropped"], 0)
            self.assertLessEqual(metrics["peak_queue"], metrics["queue_capacity"])
            self.assertLessEqual(metrics["final_queue"], metrics["queue_capacity"])

    def test_overload_window_ends_and_queue_recovers(self):
        for name in ("communication", "edge_overload", "sabotage"):
            short = run_scenario(name, Config(fault_duration=1))["metrics"]
            longer = run_scenario(name, Config(fault_duration=3))["metrics"]
            self.assertEqual(short["final_queue"], 0)
            self.assertEqual(longer["final_queue"], 0)
            self.assertGreater(longer["sensing_dropped"], short["sensing_dropped"])

    def test_redundancy_and_clock_exclusion(self):
        for name in ("node_dropout", "clock_failure"):
            result = run_scenario(name, Config(fault_duration=20))
            self.assertTrue(result["passed"])
            self.assertEqual(result["metrics"]["coasted_steps"], 0)
        self.assertEqual(
            run_scenario("clock_failure", Config(fault_duration=20))[
                "metrics"
            ]["rejected_observations"], 20,
        )

    def test_short_blackout_coasts_but_long_blackout_fails(self):
        short = run_scenario("sabotage")
        self.assertEqual(short["metrics"]["coasted_steps"], 2)
        self.assertTrue(short["passed"])
        long = run_scenario("sabotage", Config(fault_duration=5))
        self.assertFalse(long["passed"])
        self.assertEqual(long["metrics"]["lost_steps"], 2)
        self.assertIn("tracking continuity lost", long["violations"])

    def test_corruption_rejected_without_poisoning_fusion(self):
        predicted = (0.0, 0.0, 100.0)
        invalid = [
            Observation(0, None, 1),
            Observation(0, ("bad", 0, 0), 1),
            Observation(0, (float("nan"), 0, 0), 1),
            Observation(0, predicted, float("inf")),
            Observation(0, predicted, 1, 101),
            Observation(0, (100, 100, 100), 1),
            Observation(9, predicted, 1),
        ]
        valid = [Observation(node, predicted, 1) for node in range(3)]
        measured, rejected = fuse(invalid + valid + valid[:1], predicted)
        self.assertEqual(measured, predicted)
        self.assertEqual(rejected, len(invalid) + 1)
        self.assertIsNone(fuse(valid[:2], predicted)[0])
        self.assertGreater(
            run_scenario("signal_corruption")["metrics"]["rejected_observations"], 0
        )

    def test_invalid_configuration(self):
        for kwargs in (
            {"steps": 0}, {"steps": 10001}, {"steps": True},
            {"fault_duration": 0}, {"fault_duration": 37},
            {"sensing_load": 1000001}, {"seed": -1},
            {"max_tracking_error": float("nan")},
            {"max_tracking_error": float("inf")}, {"max_tracking_error": -1},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                Config(**kwargs)
        with self.assertRaises(ValueError):
            run_scenario("live_network")

    def test_cli_json_and_failure_exit(self):
        for args, expected in (
            ([], 0),
            (["--scenario", "sabotage", "--fault-duration", "5"], 1),
            (["--scenario", "baseline", "--max-tracking-error", "0"], 1),
        ):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(main(args), expected)
            self.assertTrue(json.loads(output.getvalue())["lab_only"])
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            main(["--steps", "1000000000"])
        self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
