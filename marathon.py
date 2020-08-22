# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()

    result = participant[-1]

    for i in range(len(completion)):
        if participant[i] != completion[i] :
            result = participant[i]
            break

    return result

"""
it was pretty hard for me, because of efficiency test
but i finally got pass with above code

There is Amazing code in board, so i'll copy&paste here

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]


should study bout collections
"""
