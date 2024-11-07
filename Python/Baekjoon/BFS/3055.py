# 3055. 탈출
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        r, c, time, status = q.popleft()

        if arr[r][c] == 'D':
            return time
        
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                # 물 이동
                if status == '*' and arr[nr][nc] != 'X' and arr[nr][nc] != 'D':
                    q.append((nr, nc, time + 1, '*'))
                    visited[nr][nc] = 1

                # 고슴도치 이동
                elif status == 'S' and arr[nr][nc] != 'X':
                    q.append((nr, nc, time + 1, 'S'))
                    visited[nr][nc] = 1

    return 'KAKTUS'


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

q = deque()
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            q.append((i, j, 0, '*'))  # 물 위치, 시간, 상태 저장
            visited[i][j] = 1
            
        elif arr[i][j] == 'S':  # 고슴도치 위치 파악
            hog = (i, j)
            visited[i][j] = 1

# 고슴도치 위치는 가장 마지막에 저장
q.append((*hog, 0, 'S'))

print(bfs())