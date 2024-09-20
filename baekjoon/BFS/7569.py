# 7569. 토마토
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]

    found = False
    for i in range(N):
        for j in range(M):
            for k in range(H):
                if arr[k][i][j] == 1:
                    q.append((k, i, j, 0))
                    visited[k][i][j] = 1

                if arr[k][i][j] == 0:
                    found = True
    
    if not found:
        return 0
    
    while q:
        h, r, c, days = q.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[h][nr][nc] == 0:
                q.append((h, nr, nc, days+1))
                arr[h][nr][nc] = 1
                visited[h][nr][nc] = 1
        
        for dh in [-1, 1]:
            nh = h + dh

            if 0 <= nh < H and arr[nh][r][c] == 0:
                q.append((nh, r, c, days+1))
                arr[nh][r][c] = 1
                visited[nh][r][c] = 1
    
    for i in range(N):
        for j in range(M):
            for k in range(H):
                if arr[k][i][j] == 0:
                    return -1
    
    return days


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs())