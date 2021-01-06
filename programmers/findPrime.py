from itertools import combinations

def isPrime(num) :
    if num == 1:
        return False

    for i in range(2, num+1):
        if num % i ==0 :
            return False
    return True


def solution(numbers):
    ret = 0

    numbs = []
    for num in numbers :
        numbs.append(num)

    print(list(combinations(numbs, 2)))