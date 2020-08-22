# !/usr/bin/python3 
# https://programmers.co.kr/learn/courses/30/lessons/12928


def solution(n):
    ret = list([i for i in range(1, n+1)])

    for i in ret:
        if n%i!=0:
            ret[ret.index(i)] = -1

    ret = list(filter(lambda x : x!= -1, ret))
    return sum(ret)
