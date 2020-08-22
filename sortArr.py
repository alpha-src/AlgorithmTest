# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/12915


def solution(strings, n):
    return sorted(sorted(strings), key=lambda k : k[n])


"""
Pretty Hard that should satisfy last condition
But i learned about sorted key and then i can solve it
"""
