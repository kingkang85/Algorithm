# 13038. 교환학생
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cla = list(map(int, input().split()))

    days = 1
    while n > 0:
        for c in cla:
            days += 1
            if c == 1:
                n -= 1
            
        

    