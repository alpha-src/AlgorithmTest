# !/usr/bin/env python3
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    start = 0
    end = 0
    curr = 0 # current equation
    prev = 0 # previous equation
    equations = []

    for i in range(3):
        if not list(dartResult)[start].isdigit() :
            break

        end += 3
        if end > len(dartResult)+1:
            end -=1

        eq = list(dartResult[start:end].split()[0])

        num = int(eq[0])

        if eq[0].isdigit() and eq[1].isdigit():
            end += 1
            eq = list(dartResult[start:end].split()[0])
            num = 10
            del eq[0]
            eq[0] = '10'

        start = end
        prev = curr

        if eq[1] == "S":
            curr = num ** 1
        elif eq[1] == "D":
            curr = num ** 2
        else :
            curr = num **3

        if "*" in eq :
            curr *= 2
            equations.append(curr)
            if prev == 0 :
                continue
            equations[-2] *= 2

        elif "#" in eq : 
            curr *= -1
            equations.append(curr)


        else :
            start -= 1
            end -= 1
            equations.append(curr)

    return sum(equations)
