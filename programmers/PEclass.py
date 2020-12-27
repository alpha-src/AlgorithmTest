# /usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0

    ret = []
    """
    lost : -1
    nothing : 0
    reserve : 1
    """
    
    for i in range(n+1):
        ret.append(0)

    for i in range(len(lost)):
        ret[lost[i] - 1] -= 1
    
    for i in range(len(reserve)):
        ret[reserve[i] - 1] += 1 

    for j in range(len(ret)):
        if j < n:
            if ret[j] == 1:
                if ret[j-1] == -1:
                    ret[j] = ret[j-1] = 0

                elif ret[j+1] == -1 :
                    ret[j] = ret[j+1] = 0

    ret.pop()
    answer += ret.count(0) + ret.count(1)

    return answer

