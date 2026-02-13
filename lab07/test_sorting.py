import unittest
from sorting import insertionSort, selectionSort, bubbleSort, natural_key

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.algorithms = [insertionSort, selectionSort, bubbleSort]
        self.test_cases = [
            # (Input List, Expected Result)
            ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([], []),
            ([1], [1]),
            (["banana", "apple", "cherry"], ["apple", "banana", "cherry"]),
        ]
        
        # Natural sorting cases
        self.natural_cases = [
            (["A10", "A2", "A1", "B2", "B11", "B1"], ["A1", "A2", "A10", "B1", "B2", "B11"])
        ]

    def test_standard_sort(self):
        """Test algorithms with standard data types."""
        for sort_func in self.algorithms:
            for data, expected in self.test_cases:
                with self.subTest(algorithm=sort_func.__name__, data=data):
                    arr = data.copy()
                    last = len(arr) - 1
                    # Handle empty list case
                    if last < 0:
                        steps, comps = sort_func(arr, -1)
                        self.assertEqual(arr, expected)
                        continue
                        
                    steps, comps = sort_func(arr, last)
                    self.assertEqual(arr, expected, f"{sort_func.__name__} failed for {data}")
                    self.assertIsInstance(comps, int)
                    self.assertIsInstance(steps, list)

    def test_natural_sort(self):
        """Test algorithms using the natural_key."""
        for sort_func in self.algorithms:
            for data, expected in self.natural_cases:
                with self.subTest(algorithm=sort_func.__name__, data=data):
                    arr = data.copy()
                    last = len(arr) - 1
                    sort_func(arr, last, key=natural_key)
                    self.assertEqual(arr, expected, f"{sort_func.__name__} failed natural sort for {data}")

    def test_stability_and_steps(self):
        """Verify that the steps returned represent valid intermediate states."""
        for sort_func in self.algorithms:
            data = [3, 1, 2]
            arr = data.copy()
            steps, _ = sort_func(arr, 2)
            
            # The last step should always be the sorted array
            self.assertEqual(steps[-1], sorted(data))
            # Every step should be a list of the same length
            for step in steps:
                self.assertEqual(len(step), len(data))

if __name__ == '__main__':
    unittest.main()
