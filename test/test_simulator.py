import unittest
import simulator
import yaml

class TestParallization(unittest.TestCase):
    def test_one(self):
        tasks="""
            - id: 1
              name: Task1
              duration : 3
              parallelization: 0.5
            """
        t= yaml.safe_load(tasks)
        resutl=simulator.run(t)

        self.assertEqual(resutl, 3)

    def test_two_in_parallel(self):
        tasks="""
            - id: 1
              name: Task1
              duration : 3
              parallelization: 0.5
            - id: 2
              name: Task1
              duration : 5
              parallelization: 0.5
            """
        t= yaml.safe_load(tasks)
        result=simulator.run(t)

        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
