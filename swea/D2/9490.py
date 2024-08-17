# 9490. 풍선팡
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            baseV = arr[i][j]
            for k in range(1, baseV+1):
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni = i + di * k
                    nj = j + dj * k

                    if 0 <= ni < N and 0 <= nj < M:
                        baseV += arr[ni][nj]
  
            if maxV < baseV:
                maxV = baseV
        
    print(f'#{tc} {maxV}')