import unittest
import simulator
import yaml


class TestParallization(unittest.TestCase):
    def test_one(self):
        tasks = """
            - duration : 3
              parallelization: 0.5
            """
        t = yaml.safe_load(tasks)
        resutl = simulator.run(t)

        self.assertEqual(resutl, 3)

    def test_two_in_parallel(self):
        tasks = """
            - duration : 3
              parallelization: 0.5
            - duration : 5
              parallelization: 0.5
            """

    def test_tree_semi_parallel(self):
        tasks = """
            - duration : 3
              parallelization: 0.5
            - duration : 5
              parallelization: 1
            - duration : 5
              parallelization: 0.5
            """
        t = yaml.safe_load(tasks)
        result = simulator.run(t)

        self.assertEqual(result, 10)


class TestDependencies(unittest.TestCase):
    def test_after_one(self):
        tasks = """
            - id: 1
              duration : 3
              parallelization: 0.5
            - duration: 4
              parallelization: 0.5
              after: 1
            """
        t = yaml.safe_load(tasks)
        result = simulator.run(t)

        self.assertEqual(result, 7)

    def test_mix_depends_and_parallel(self):
        cases = [
            {"tasks": """
                - id: 1
                  duration : 3
                  parallelization: 0.5
                - id: 2
                  duration : 5
                  parallelization: 0.5
                  after: 1
                - id: 3
                  duration : 5
                  parallelization: 0.5
                  after: 2
                - id: 4
                  duration : 5
                  parallelization: 0.5
                  after: 2
                """,
             "expect": 13},
            {"tasks": """
                - id: 1
                  duration : 3
                  parallelization: 0.5
                - id: 2
                  duration : 5
                  parallelization: 0.5
                  after: 1
                - id: 3
                  duration : 5
                  parallelization: 0.5
                  after: 2
                - id: 4
                  duration : 5
                  parallelization: 0.6
                  after: 2
                """,
             "expect": 18}
        ]

        for i in range(len(cases)):
            c = cases[i]
            t = yaml.safe_load(c["tasks"])
            result = simulator.run(t)
            self.assertEqual(result, c["expect"], f"Test fail in case {i}")


class TestValidation(unittest.TestCase):
    def test_not_duplicated_id(self):
        tasks = """
            - id: 1
              duration : 3
              parallelization: 0.5
            - id: 1
              duration: 4
              parallelization: 0.5
              after: 1
            """
        t = yaml.safe_load(tasks)

        with self.assertRaises(Exception):
            simulator.run(t)


if __name__ == '__main__':
    unittest.main()
