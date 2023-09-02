def solution(s):
    # 괄호의 짝이 맞으려면 무조건 짝수여야 하므로, 선제적으로 괄호의 길이를 평가합니다.
    if len(s) % 2 != 0:
        return False

    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
