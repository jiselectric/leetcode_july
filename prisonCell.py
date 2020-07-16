def solution(cells, N):
    stack = []
    number = 0
    
    if N % 14 == 0:
        N = 14
    else:
        N = N % 14

    while number < N:
        stack = []
        for i in range(0, len(cells) - 1):
            if len(stack) == 0:
                stack.append(0)
            else:
                temp = cells[i-1]
                if temp == cells[i+1]:
                    stack.append(1)
                else:
                    stack.append(0)
        number += 1
        stack.append(0)
        cells = stack
        

    return stack



cells = [0,0,0,1,1,0,1,0]
N = 788566492   
# [0,0,1,1,1,1,1,0]

print(solution(cells, N))