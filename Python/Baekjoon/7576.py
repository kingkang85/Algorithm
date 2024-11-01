# 7576. 토마토
from collections import deque
import sys
input = sys.stdin.readline

def bfs(str, stc):
    q = deque([(str, stc)])
    visited[str][stc] = 1

    while q:
        r, c = q.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nr < N and visited[nr][nc] == 0 and arr[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
                tomatoes.append((nr, nc))
    

                

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

days = 0
while True:
    visited = [[0] * N for _ in range(M)]
    tomatoes = []
    found = False
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                tomatoes.append((i, j))
                bfs(i, j)
    
    for r, c in tomatoes:
        arr[r][c] = 1

# 쥐민! 토메이도 잘 익혀 먹어~