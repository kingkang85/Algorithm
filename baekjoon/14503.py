# 14503. 로봇 청소기
from collections import deque

def bfs(i, j, d):
    visited = [[0] * M for _ in range(N)]
    dq = deque()
    dq.append([i, j])
    visited[i][j] = 1
    
    cnt = 0
    while dq:
        ti, tj = dq.popleft()
        print(ti, tj)
        cnt += 1
        if room[ti][tj] == 1:
            return cnt
        
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        
        ni = ti + di[d]
        nj = tj + dj[d]

        if 0 <= ti < N and 0 <= tj < M and room[ni][nj] == 0 and visited[ni][nj] == 0:
            d = (d+1) % 4
            dq.append([ni, nj])
            visited[ni][nj] = 1
        


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

print(bfs(r, c, d))
