def quick_sort(nums: list[int], start: int = 0, end: int = None) -> list[int]:
    if end is None:
        end = len(nums) - 1

    if start >= end:
        return nums

    pivot = end
    pivot_value = nums[pivot]

    left = start

    for right in range(start, end):
        if nums[right] < pivot_value:
            retVal = nums[left]
            nums[left] = nums[right]
            nums[right] = retVal
            left += 1

    retVal = nums[left]
    nums[left] = nums[pivot]
    nums[pivot] = retVal

    quick_sort(nums, start, left - 1)
    quick_sort(nums, left + 1, end)

    return nums

    
import unittest

class test_quick_sort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_two_elements_swapped(self):
            self.assertEqual(quick_sort([2, 1]), [1, 2])
    
    def test_two_elements_ordered(self):
        self.assertEqual(quick_sort([1, 2]), [1, 2])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(quick_sort([4, 6, 2, 1, 10]), [1, 2, 4, 6, 10])

    def test_duplicates(self):
        self.assertEqual(quick_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(quick_sort([0, -3, 5, -1, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal(self):
        self.assertEqual(quick_sort([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_min_at_end(self):
        self.assertEqual(quick_sort([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])

    def test_max_at_start(self):
        self.assertEqual(quick_sort([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_sorts_original_list(self):
        nums = [4, 3, 2, 1]
        original_id = id(nums)

        result = quick_sort(nums)

        self.assertEqual(nums, [1, 2, 3, 4])
        self.assertEqual(id(nums), original_id)
        self.assertIs(result, nums)

    def test_sorts_original_list_with_duplicates(self):
        nums = [3, 1, 2, 1]
        quick_sort(nums)

        self.assertEqual(nums, [1, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()