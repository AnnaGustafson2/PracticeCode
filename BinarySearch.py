def binary_search(nums: list[int], target: int) -> int:
    if nums is None or len(nums) == 0:
        return None

    middle = len(nums) // 2
    if nums[middle] == target:
        return middle
    
    elif nums[middle] < target:
        search = binary_search(nums[middle + 1:], target)
        return search if search is None else middle + 1 + search
    else:
        return binary_search(nums[:middle], target)

import unittest

class test_binary_search(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(binary_search([], 0), None)

    def test_found(self):
       self.assertEqual(binary_search([1, 2, 3, 4], 2), 1)

    def test_not_found(self):
       self.assertEqual(binary_search([1, 2, 3, 4], 5), None)

    def test_begining(self):
       self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)

    def test_end(self):
       self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)

if __name__ == "__main__":
    unittest.main()
    