import unittest
import simulator
import yaml

class TestParallization(unittest.TestCase):
    def test_one(self):
        tasks="""
            - duration : 3
              parallelization: 0.5
            """
        t= yaml.safe_load(tasks)
        resutl=simulator.run(t)

        self.assertEqual(resutl, 3)

    def test_two_in_parallel(self):
        tasks="""
            - duration : 3
              parallelization: 0.5
            - duration : 5
              parallelization: 0.5
            """
    def test_tree_semi_parallel(self):
        tasks="""
            - duration : 3
              parallelization: 0.5
            - duration : 5
              parallelization: 1
            - duration : 5
              parallelization: 0.5
            """
        t= yaml.safe_load(tasks)
        result=simulator.run(t)

        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
