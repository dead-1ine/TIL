def solution(s):
    words = s.split(" ")
    jaden_case_words = []

    for word in words:
        if len(word) > 0:
            jaden_case_words.append(word[0].upper() + word[1:].lower())
        else:
            jaden_case_words.append('')

    return " ".join(jaden_case_words)


if __name__ == '__main__':
    for s in ["3people unFollowed me", "for the last week"]:
        print(solution(s))