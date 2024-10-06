# 22683. 나무 베기
from collections import deque

def bfs():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = deque([(start[0], start[0], 0, 0, 0)])  # 시작위치, 방향, 나무 벤 횟수, 조작 횟수
    visited = set([(start[0], start[1], 0, 0)])  # 시작위치, 방향, 나무 벤 횟수

    while q:
        r, c, d, cut, steps = q.popleft()

        if (r, c) == end:
            return steps

        # 앞으로 전진
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] in 'GXY' and (nr, nc, d, cut) not in visited:
                q.append((nr, nc, d, cut, steps+1))
                visited.add((nr, nc, d, cut))

            elif arr[nr][nc] == 'T' and cut < K and (nr, nc, d, cut+1) not in visited:
                q.append((nr, nc, d, cut+1, steps+1))
                visited.add((nr, nc, cut+1, d))

        # 좌회전 or 우회전
        for direct in ((d - 1) % 4, (d + 1) % 4):
            if (r, c, direct, cut) not in visited:
                q.append((r, c, direct, cut, steps+1))
                visited.add((r, c, direct, cut))

    return -1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 시작 위치와 도착 위치 찾기
    start = end = None
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
            
            elif arr[i][j] == 'Y':
                end = (i, j)
    
    print(f'#{tc} {bfs()}')