def solution(nums: list):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)

    return False


print(solution([1, 2, 3, 4, 5, 6, 6, 1, 2]))

print(solution([1, 2, 3]))

