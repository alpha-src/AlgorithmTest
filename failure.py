# !/usr/bin/env python3
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages) :
    count = 0
    people = len(stages) 

    ret = {}

    for lvl in set(stages):
        count = stages.count(lvl)
        if lvl == N+1:
            people -= count
            continue

        ret[lvl] = count/people
        people -= count

    ret = dict(sorted(ret.items(), key=lambda x : x[1], reverse= True))

    for i in range(1, N+1):
        if i not in ret.keys():
            ret[i] = 0

    if len(ret) != N:
        for i in range(1, N):
            ret[i] = 0

    return list(ret.keys())
