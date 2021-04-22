import unittest
import find_holds
import numpy as np

class TestFindHolds(unittest.TestCase):

    def test_possible_configurations(self):
        climbing_face = [(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0), (2.0, 1.0, 0.0), (2.0, 2.0, 0.0)]
        initial_holds = [(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)]
        goal_hold = (2.0, 2.0, 0.0)
        shortest_path = find_holds.get_possible_holds(climbing_face, initial_holds)
        expected = [((1.0, 1.0, 0.0), (2.0, 1.0, 0.0))]

        self.assertEqual(shortest_path, expected)

    def test_find_shortest_path(self):
        climbing_face = [(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0), (2.0, 1.0, 0.0), (2.0, 2.0, 0.0)]
        initial_holds = [(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)]
        goal_hold = (2.0, 2.0, 0.0)
        shortest_path = find_holds.shortest_path(climbing_face, initial_holds=initial_holds, goal_hold=goal_hold)
        expected = [(1.0, 1.0, 0.0), (2.0, 1.0, 0.0), (2.0, 2.0, 0.0)]
        self.assertEqual(shortest_path, expected)

if __name__ == '__main__':
    unittest.main()