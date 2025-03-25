# 게임 맵 최단거리
from collections import deque

def bfs(n, m, maps):
    visited = [[0] * m for _ in range(n)]
    
    q = deque([(0, 0, 1)])
    visited[0][0] = 1

    while q:
        r, c, dist = q.popleft()
        
        if r == n-1 and c == m-1:
            return dist

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and maps[nr][nc] == 1:
                q.append((nr, nc, dist + 1))
                visited[nr][nc] = 1

    return -1

def solution(maps):
    n = m = 0
    for _ in maps:
        n += 1
    
    for _ in maps[0]:
        m += 1
    
    return bfs(n, m, maps)