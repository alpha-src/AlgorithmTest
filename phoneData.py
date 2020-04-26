# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True

    ret = min(phone_book)

    for i in range(len(phone_book)):
        if ret != phone_book[i]:
            if ret in phone_book[i]:
                answer = False

    return answer
