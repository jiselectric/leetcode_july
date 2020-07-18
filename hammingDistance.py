def solution(x, y):
    xor = x ^ y
    distance = 0 

    while xor:
        if xor & 1:
            distance += 1
        xor = xor >> 1
    
    return distance

x, y = 1, 4
print(solution(x, y))