# /usr/bin/python3


def solution(board, moves):
    baguni = [] 
    answer = 0

    for i in moves:
        for j in range(len(board[i-1])):
            item = board[j][i-1]
            
            if item == 0:
                continue

            else :
                baguni.append(item)
                if len(baguni) >= 2 :
                    if baguni[-2] == item:
                        answer += 1
                        del baguni[-1]
                        del baguni[-1]
                        
                board[j][i-1] = 0
                break


    return answer*2


