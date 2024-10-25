# 2589. 보물섬
from collections import deque
import sys
input = sys.stdin.readline

def find_land():
    maxD = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                maxD = bfs(i, j, maxD)
    print(maxD)

def bfs(str, stc, maxD):
    q = deque([(str, stc, 0)])
    visited = [[-1] * M for _ in range(N)]
    visited[str][stc] = 0

    while q:
        r, c, dist = q.popleft()
        
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1 and arr[nr][nc] == 'L':
                q.append((nr, nc, dist+1))
                visited[nr][nc] = dist+1
    
    for row in visited:
        for col in row:
            if maxD < col:
                maxD = col
    
    return maxD
                
N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

land_lst = []
find_land()

####################################################################################################
from collections import deque
import sys
input= sys.stdin.readline

def bfs(str, stc):
    q = deque([(str, stc)])
    visited = [[-1] * M for _ in range(N)]
    visited[str][stc] = 0
    
    cnt = 0
    while q:
        r, c = q.popleft()
        
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1 and arr[nr][nc] == 'L':
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                cnt = max(cnt, visited[nr][nc])
    return cnt

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

maxD = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            maxD = max(maxD, bfs(i, j))

print(maxD)