# 14503. 로봇 청소기
from collections import deque

def bfs(i, j, d):
    visited = [[0] * M for _ in range(N)]
    dq = deque()
    dq.append([i, j])
    visited[i][j] = 1
    
    cnt = 1
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    while True:
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 and visited[ni][nj] == 0:
            dq.append([ni, nj])
            cnt += 1
            d = (d+3) % 4
            visited[ni][nj] = 1
        
        else:
            if dq:
                i, j = dq.popleft()
                if room[i][j] == 1:
                    return cnt

        

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

print(bfs(r, c, d))
