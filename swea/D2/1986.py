# 1986. 지그재그 숫자
t = int(input())

for i in range(t):
    n = int(input())
    
    sum = 0  # 반복마다 sum 초기화
    for j in range(1, n+1):
        if j % 2 == 1:  # 홀수일 때
            sum += j
        else:           # 짝수일 때
            sum -= j
        
    print(f'#{i+1} {sum}')