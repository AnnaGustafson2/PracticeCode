def BubbleSort(nums: list[int]) -> list[int]:
    for loop in range(len(nums)):
        swapped = False

        for i in range(len(nums) - loop - 1):
            if nums[i + 1] < nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        if not swapped:
            break

    return nums


if __name__ == "__main__":
    print("Result for [4, 3, 2]:", BubbleSort([4, 3, 2]))  
    print("Result for [4, 6, 2, 1, 10]:", BubbleSort([4, 6, 2, 1, 10])) 