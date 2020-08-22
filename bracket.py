# https://programmers.co.kr/learn/courses/30/lessons/60058
# !/bin/python3

def bracket_check(a):
    if not a:
        return True

    stack = [] 
    for bracket in a: 
        if bracket == '(': 
            stack.append(bracket)

        else:
            if not stack:
                return False
            stack.pop() 

    if not stack :
        return True

    return False

def slice_str(a):
    left = 0
    right = 0
    index = 0 

    for bracket in a:
        index += 1

        if bracket == '(':
            left += 1
        else:
            right += 1

        if left == right:
            break

    return index

def legitBracket(u):  # u가 올바른 괄호 문자열이 아닐 때
    res = ""

    new_str = u[1: -1]
    for bracket in new_str :
        if bracket == "(":
            res += ")"
        else:
            res += "("

    return res

def solution(p):
    if bracket_check(p):
        return p
    ans = ""

    if not p:
        return ans

    index = slice_str(p)

    u = p[0:index]
    v = p[index:]

    if bracket_check(u): #u가 올바를 때
        ans += u
        ans += solution(v) 

    else:
        ans = "("
        ans += solution(v)
        ans += ")"
        ans += legitBracket(u)

    return ans