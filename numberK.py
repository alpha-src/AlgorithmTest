# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/42748#



def solution(array, commands):
    answer = []
    cnt = len(commands)
    print(cnt)

    for i in range(cnt):
        k = commands[i][2]
        tmp = commands[i]
        ret = array[tmp[0]-1 : tmp[1]]
        ret.sort()
        answer.append(ret[k-1])

    return(answer)
