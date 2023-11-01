# with Hash table

# 1st Args
# input:
#   nums = {4,1,9,7,5,3,16}
#   target: 14
# output: True

def solution(nums, target):
	nums_dict = {}
	for num in nums:
		nums_dict[f'{num}'] = True

	for num in nums:
		# num이 target보다 크거나 같으면 안됨
		# if num >= target:
		# 	continue

		target_num = target - num
		if target_num in nums_dict:  # O(1): hash table을 사용하여 바로 인덱스에 접근하기 때문
			return True

	return False


print(solution(nums={4, 1, 9, 7, 5, 3, 16}, target=14))

print(solution(nums={4, 1}, target=14))
