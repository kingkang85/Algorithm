# 14503. 로봇 청소기
from collections import deque

def bfs(i, j, d):
    visited = [[0] * M for _ in range(N)]
    dq = deque()
    dq.append([i, j])
    visited[i][j] = 1
    ri = [-1, 0, 1, 0]
    ci = [0, 1, 0, -1]

    cnt = 1
    while dq:
        ti, tj = dq.popleft()

        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = ti + di, tj + dj

            if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 and visited[ni][nj] == 0:
                d = (d+3) % 4
                newi, newj = ti + ri[d], tj + ci[d]
                if visited[newi][newj] == 0:
                    cnt += 1
                    dq.append([newi, newj])
                    visited[newi][newj] = 1
                    
                
            else:
                newr, newc = ti + ri[d], tj + ci[d]
                if room[newr][newc] == 1:
                    return cnt
                else:
                    dq.append([newr, newc])
                    visited[newr][newc] = 1


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

print(bfs(r, c, d))
