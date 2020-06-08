#!/usr/bin/python3 
# https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):

    answer = 0
    
    for skills in skill_trees :
        skillSplit = list(skills)

        for i in range(len(skillSplit)):
            if skillSplit[i] not in skill :
                skills = skills.replace(skillSplit[i], "")
                
        if len(skills) == 0:
            answer +=1
            print("pass : ", "".join(skillSplit))
            continue;

        if skills in skill :
            if list(skills)[0] == list(skill)[0] :
                answer +=1
                print("pass : ", "".join(skillSplit))
        
    return answer

if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "ASF", "BDF", "CEFD", "CXF"]

    print(solution(skill, skill_trees))



"""
Should think about exception 

1. if skill_trees don't include essential skill tree answer's add 1
2. if skill_trees don't start with essential skill tree[0], it's not including in answer

"""
