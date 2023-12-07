from functools import cmp_to_key


def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers_str = [str(num) for num in numbers]

    # 두 문자열을 이어붙였을 때 더 큰 쪽이 앞으로 오도록 정렬
    numbers_str.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))

    # 정렬된 문자열들을 이어붙여 결과를 반환
    # 단, 결과가 "0000"과 같이 모두 0인 경우에는 "0"을 반환
    answer = ''.join(numbers_str)

    return answer if answer[0] != '0' else '0'


# 테스트
numbers = [6, 10, 2]
print(solution(numbers))  # 출력: "6210"

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))  # 출력: "9534330"