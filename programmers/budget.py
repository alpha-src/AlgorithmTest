# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

def solution(d, budget) :
    ret = []

    while(sum(ret) <= budget):
        if len(d) == 0:
            break
        a = min(d)
        ret.append(a)
        if sum(ret) > budget:
            ret.pop()
            break
        del d[d.index(a)]

    return len(ret)
