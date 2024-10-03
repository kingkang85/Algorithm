# 14503. 로봇 청소기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0  # 청소한 칸 개수
direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:
    # 청소되지 않은 경우(0) 청소(2)
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    
    # 반시계 방향으로 돌며 주변에 청소되지 않은 칸이 있는지 탐색
    for _ in range(4):
        d = (d+3) % 4
        nr, nc = r + direct[d][0], c + direct[d][1]

        # 청소되지 않은 칸이 있다면 청소하러 보내자
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
           r, c = nr, nc
           break

    # 주변에 청소되지 않은 빈 칸이 없는 경우          
    else:
        nr, nc = r - direct[d][0], c - direct[d][1]  # 한 칸 후진

        # 벽이 아니라면 청소하러 보내자
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
            r, c = nr, nc
        
        # 벽이면 중단
        else:
            break
    
print(cnt)