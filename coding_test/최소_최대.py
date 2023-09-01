def solution(s):
    s = [int(x) for x in s.split(' ')]
    return f"{min(s)} {max(s)}"


if __name__ == '__main__':
    for s in ['1 2 3 4', '-1 -2 -3 -4', '-1 -1']:
        print(solution(s))