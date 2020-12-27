# https://programmers.co.kr/learn/courses/30/lessons/12926
# !/usr/bin/python3


def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = list(alpha)
    ans = []
    str = list(s)

    for char in str:
        if char == ' ':
            ans.append(char)
            continue
            
        idx = alpha.index(char.lower()) + n

        if idx >= 26 :
            idx = idx%26

        ans.append(alpha[idx])

        if char.isupper() :
            ans.pop()
            ans.append(alpha[idx].upper())
        continue

        ans.append(alpha[idx])

    return ''.join(ans)
