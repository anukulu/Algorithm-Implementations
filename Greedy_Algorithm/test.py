import unittest
from greedyAlgorithm import ActivitySelectionIterative, ActivitySelectorRecursive, EventsSort

class GreedyAlgorithmTest(unittest.TestCase):
    
    def test_activity_selection_iterative(self):
        events = [[1,2],[3,4],[0,6],[5,7],[8,9],[5,9]]
        index = [0, 1, 3, 4]
        self.assertListEqual(ActivitySelectionIterative(events,0),index)
    def test_activity_selection_recursive(self):
		events = [[1,2],[3,4],[0,6],[5,7],[8,9],[5,9]]
        index = [0, 1, 3, 4]
        self.assertListEqual(ActivitySelectorRecursive(events,-1, len(events)),index)
if __name__ == '__main__':
    unittest.main()