def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    sum_value = 0
    for i in range(len(A)):
        sum_value += A[i] * B[i]

    return sum_value


if __name__ == '__main__':
    for A, B in [
        ([1, 4, 2], [5, 4, 4]),
        ([1, 2], [3, 4]),
    ]:
        print(solution(A, B))