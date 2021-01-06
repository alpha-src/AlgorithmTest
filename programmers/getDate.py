# !/usr/bin/python3
# https://programmers.co.kr/learn/courses/30/lessons/12901#

def solution(a,b) :
    answer =''

    days31 = [1,3,5,7,8,10,12]
    days30 = [4,6,9,11]
    days29 = 2
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    
    currentMonth = 1
    currentDay = days[5]

    while currentMonth != a :
        if currentMonth in days31 :
            mod = 31%7 - 1
        elif currentMonth == days29:
            mod = 29%7 - 1
        else :
            mod = 30%7 - 1

        if days.index(currentDay) + mod > 6 :
            currentDay = days[days.index(currentDay) + mod -7]
        
        else :
            currentDay = days[days.index(currentDay) + mod]
        
        if currentDay == "SAT":
            currentDay = "SUN"
        else :
            currentDay = days[days.index(currentDay) + 1]

        currentMonth += 1


    cnt = b%7 - 1
    chk  = days.index(currentDay) + cnt
    
    if chk > 6:
        currentDay = days[chk%7]
        
    else :
        currentDay = days[chk]

    answer = currentDay

    return answer


"""Another Solution

#! /usr/bin/python3

import calendar

def solution(a,b) :
    days = ["MON","TUE","WED","THU","FRI","SAT", "SUN"]

    ret= calendar.weekday(2016, a, b)
    return days[ret]
"""