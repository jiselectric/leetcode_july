def solution(n):
    answer = 1
    k = 1

    if n == 1:
        return 1

    while n >= k:
        answer = answer + 1

        n = n - k
        
        k = k + 1

    return answer - 1

n = 18
print(solution(n))