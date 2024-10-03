# 12368. 24시간
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    
    time = a + b
    
    if time >= 24:   # 더한 값이 24 이상이면,
        time -= 24   # 24를 빼서 24시간제로 변환
    
    print(f'#{i+1} {time}')