def solution(n):
        list = [1]
        
        idx2, idx3, idx5 = 0, 0, 0
        
        for i in range(n - 1):
            next2 = list[idx2] * 2
            next3 = list[idx3] * 3
            next5 = list[idx5] * 5
            
            next = min(next2, next3, next5)
            list.append(next)
            
            if next == next2:
                idx2 += 1
            if next == next3:
                idx3 += 1
            if next == next5:
                idx5 += 1
                
        return list[-1]

n = 10
# 12 
print(solution(n))