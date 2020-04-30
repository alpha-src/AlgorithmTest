# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s = s.lower()
    strList = list(s)
    ans = ''

    cnt = 0

    for char in strList:
        ans += char
        if char == ' ':
            cnt = 0
            continue

        if cnt%2==0:
            ans = ans[:-1]
            ans += char.upper()

        cnt +=1

    return ans
