def solution(arr):
	stack = [arr[0]]
	for x in arr[1:]:
		stack_tail = stack[-1]
		if x != stack_tail:
			stack.append(x)
	return stack


print(solution([1,1,3,3,0,1,1]))
