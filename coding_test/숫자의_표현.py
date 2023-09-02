def solution(n):
    answer = 0  # 연속된 자연수로 n을 표현하는 방법의 수

    for length in range(1, int((2 * n) ** 0.5) + 1):  # 가능한 연속된 수의 길이
        if (n - (length * (length - 1) // 2)) % length == 0:  # 조건을 만족하면
            answer += 1  # 방법의 수를 하나 증가

    return answer  # 답을 반환


print(solution(15))