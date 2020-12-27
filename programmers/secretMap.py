# ! /usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    ret = []
    
    for i in range(n):
        tmp = arr1[i] | arr2[i]
        tmp = format(tmp, 'b')
        
        if len(tmp) != n:
            tmp = '0'*(n - len(tmp)) + tmp
            
        ret.append(tmp)
        ret[i] = ret[i].replace("1", "#")
        ret[i] = ret[i].replace("0", " ")
        
        
    return ret
