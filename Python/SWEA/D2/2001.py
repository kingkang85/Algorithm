# 2001. 파리 퇴치
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열

    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            sum_v = 0  # 배열의 각 원소마다 초기화
            for i2 in range(i, i+M): 
                for j2 in range(j, j+M):  # M x M 만큼 파리 죽이기
                    sum_v += arr[i2][j2]
            
            if Max < sum_v:
                Max = sum_v
    
    print(f'#{tc} {Max}')
