def solution(string):
    chars = list(string)
    chars.reverse()
    return ''.join(chars)

print(solution("world"))