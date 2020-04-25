# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    answer = []
    
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            arr[i-1] = -1
    
    answer = list(filter(lambda a: a != -1, arr))
    return answer
