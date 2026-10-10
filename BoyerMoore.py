def BoyerMoore(nums: list[int]) -> int | None:
    candidate = None
    count = 0

    for n in nums:
        if count == 0:
            candidate = n
            count = 1
        elif candidate == n:
            count += 1
        else:
            count -= 1

    final_count = 0
    for n in nums:
        if n == candidate:
            final_count += 1

    if final_count > len(nums) // 2:
        return candidate
    return None

if __name__ == "__main__":
    print("Result for [1, 2, 3]:", BoyerMoore([1, 2, 3]))  
    print("Result for [2, 2, 1, 1, 2]:", BoyerMoore([2, 2, 1, 1, 2]))