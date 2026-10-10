def MergeSort(nums: list[int]) -> list[int]:
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    middle = len(nums) // 2
    left = MergeSort(nums[:middle])
    right = MergeSort(nums[middle:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

import unittest

class MergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(MergeSort([]), [])

    def test_single_element(self):
        self.assertEqual(MergeSort([5]), [5])

    def test_two_elements_swapped(self):
            self.assertEqual(MergeSort([2, 1]), [1, 2])
    
    def test_two_elements_ordered(self):
        self.assertEqual(MergeSort([1, 2]), [1, 2])

    def test_sorted_list(self):
        self.assertEqual(MergeSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(MergeSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(MergeSort([4, 6, 2, 1, 10]), [1, 2, 4, 6, 10])

    def test_duplicates(self):
        self.assertEqual(MergeSort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(MergeSort([0, -3, 5, -1, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal(self):
        self.assertEqual(MergeSort([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_min_at_end(self):
        self.assertEqual(MergeSort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])

    def test_max_at_start(self):
        self.assertEqual(MergeSort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()