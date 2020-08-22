# ! /usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    answer = sorted(list(filter(lambda x:x%divisor==0, arr)))
    
    if not answer:
        answer.append(-1)
        
    return answer
