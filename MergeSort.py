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

if __name__ == "__main__":
    print("Result for [4, 3, 2]:", MergeSort([4, 3, 2]))  
    print("Result for [4, 6, 2, 1, 10]:", MergeSort([4, 6, 2, 1, 10])) 
    print("Result for [9, 4, 6, 2, 1, 10]:", MergeSort([9, 4, 6, 2, 1, 10]))