def linear_search(nums: list[int], target: int) -> int:
    if not nums:
        return None
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return None
import unittest

class test_linear_search(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(linear_search([], 0), None)

    def test_found(self):
            self.assertEqual(linear_search([1, 2, 3, 4], 2), 1)

    def test_not_found(self):
                self.assertEqual(linear_search([1, 2, 3, 4], 5), None)

    def test_begining(self):
                    self.assertEqual(linear_search([1, 2, 3, 4], 1), 0)

    def test_end(self):
                        self.assertEqual(linear_search([1, 2, 3, 4], 4), 3)

if __name__ == "__main__":
    unittest.main()