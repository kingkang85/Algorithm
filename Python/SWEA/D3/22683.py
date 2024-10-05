# 22683. 나무 베기
from collections import deque

def bfs():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = deque([(start[0], start[1], 0, 0, 0)])
    visited = set([(start[0], start[1], 0, 0)])

    while q:
        r, c, d, cut, steps = q.popleft()

        if (r, c) == end:
            return steps
        
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] in 'GYX' and (nr, nc, d, cut) not in visited:
                q.append((nr, nc, d, cut, steps + 1))
                visited.add((nr, nc, d, cut))

            elif arr[nr][nc] == 'T' and cut < K and (nr, nc, d, cut + 1) not in visited:
                q.append((nr, nc, d, cut + 1, steps + 1))
                visited.add((nr, nc, d, cut + 1))
        
        for new_d in ((d - 1) % 4, (d + 1) % 4):
            if (r, c, new_d, cut) not in visited:
                q.append((r, c, new_d, cut, steps + 1))
                visited.add((r, c, new_d, cut))
        
    return -1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)

            elif arr[i][j] == 'Y':
                end = (i, j)

    print(f'#{tc} {bfs()}')