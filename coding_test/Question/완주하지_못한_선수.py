# THINKING:
#   1. 문제를 직관적으로 이해해보자. 굳이 어렵게 돌아가는 것 같다.

# 1. 우선 문제를 직관화

# completions = ["mislav", "stanko", "mislav", "ana"]

# comple_hash = {}
# for completion in completions:
# 	comple_hash[completion] = completions.count(completion)
	# 하지만 list.count()는 O(n)이다. -> n^5가 들어오면 => 극단화
	# list의 수 = n, list.count() = n => n^2
	# 시간복잡도 조건에 맞지 않지만 한번 풀어나봐보자. => 단순화

#
# def solution(participants, completions):
# 	# Make hash table with dict
# 	participant_hash = {}
# 	for x in participants:  # O(n) * O(n) = O(n^2)
# 		dupl_cnt = participants.count(x)  # O(n)
# 		participant_hash[x] = dupl_cnt
#
# 	for completion in completions:  # O(n)
# 		participant_dupl_cnt = participant_hash[completion]
#
# 		if participant_dupl_cnt >= 1:
# 			participant_hash[completion] -= 1
# 		elif participant_dupl_cnt == 0:
# 			return completion
#
#
# print(solution(participants=["mislav", "stanko", "mislav", "ana"], completions=["stanko", "ana", "mislav"]))


# completions = ["stanko", "ana", "mislav"]
#
# participant_hash = {
# 	'mislav': 2,
# 	'stanko': 1,
# 	'ana': 1
# }
#
# for completion in completions:  # O(n)
# 	participant_dupl_cnt = participant_hash[completion]
#
# 	if completion not in participant_hash:
# 		print(completion)
#
# 	if participant_dupl_cnt >= 1:
# 		 participant_hash[completion] -= 1
# 	elif participant_dupl_cnt == 0:
# 		print(completion)
#

# 정답 1
def solution(participant, completion):
	answer = {}
	for i in participant:
		answer[i] = answer.get(i, 0) + 1
	for j in completion:
		answer[j] -= 1

	for k in answer:
		if answer[k]:
			return k


# print(solution(participant=["mislav", "stanko", "mislav", "ana"], completion=["stanko", "ana", "mislav"]))

# # 정답 2 - hash()를 사용하여 hash 값을 모두 더하고 뺏을 때 마지막에 남은 숫자가 완주하지 못한 사람의 해시값.
# def solution(participant, completion):
# 	value = 0
# 	answer = {}
# 	for part in participant:
# 		answer[hash(part)] = part
# 		value += int(hash(part))
# 	for comp in completion:
# 		value -= hash(comp)
#
# 	return answer[value]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

hash_table = {}
for i in participant:
	hash_table[i] = hash_table.get(i, 0) + 1

print(hash_table)

