# /usr/bin/python3 
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    

    """ 
    student 1 : 1,2,3,4,5 and so on...
    student 2 : 2, 1, 2, 3, 2, 4, 2, 5 and so on...
    student 3 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 and so on...

    """


    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    a = len(A)
    b = len(B)
    c = len(C)


    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(len(answers)) :
        if i >=a :
            if answers[i]==A[i%a]:
                sum1+=1
        else:
            if answers[i]==A[i%a]:
                sum1+=1

    for i in range(len(answers)) :
        if i >=b :
            if answers[i]==B[i%b]:
                sum2+=1
        else:
            if answers[i]==B[i%b]:
                sum2+=1


    for i in range(len(answers)) :
        if i >=c:
            if answers[i]==C[i%c]:
                sum3+=1

        
        
    result = []

    if max(sum1, sum2, sum3) == sum1 :
        result.append(1)

    if max(sum1, sum2, sum3) == sum2:
        result.append(2)

    if max(sum1, sum2, sum3) == sum3:
        result.append(3)

    return result


    """
    Got passed by above code, but it's pretty massy
    should study bout enumerate

    """
