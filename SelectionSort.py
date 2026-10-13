def selection_sort(nums: list[int]) -> list[int]:
    left = 0
    while left < len(nums) - 1:
        minimum = left
        for index in range(left + 1, len(nums)):
            if nums[index] < nums[minimum]:
                minimum = index

        nums[minimum], nums[left] = nums[left], nums[minimum]
        left += 1
    return nums

import unittest

class TestSelectionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([5]), [5])

    def test_two_elements_swapped(self):
            self.assertEqual(selection_sort([2, 1]), [1, 2])
    
    def test_two_elements_ordered(self):
        self.assertEqual(selection_sort([1, 2]), [1, 2])

    def test_sorted_list(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(selection_sort([4, 6, 2, 1, 10]), [1, 2, 4, 6, 10])

    def test_duplicates(self):
        self.assertEqual(selection_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(selection_sort([0, -3, 5, -1, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal(self):
        self.assertEqual(selection_sort([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_min_at_end(self):
        self.assertEqual(selection_sort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])

    def test_max_at_start(self):
        self.assertEqual(selection_sort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_sorts_original_list(self):
        nums = [4, 3, 2, 1]
        original_id = id(nums)

        result = selection_sort(nums)

        self.assertEqual(nums, [1, 2, 3, 4])
        self.assertEqual(id(nums), original_id)
        self.assertIs(result, nums)

    def test_sorts_original_list_with_duplicates(self):
        nums = [3, 1, 2, 1]
        selection_sort(nums)

if __name__ == "__main__":
    unittest.main()