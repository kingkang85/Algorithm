# 2573. 빙산
from collections import deque
import sys
input = sys.stdin.readline

# 빙산 덩어리 나누는 함수
def check():
    q = deque()
    visited = [[0] * M for _ in range(N)]
    islands = 0  # 빙산 덩어리 수

    for i in range(1, N-1):
        for j in range(1, M-1):
            if visited[i][j] == 0 and arr[i][j] != 0:
                islands += 1
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    r, c = q.popleft()
                    for dr, dc in direct:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
    
    if islands >= 2:
        return True
    return False

# 빙산 녹이는 함수
def bfs():
    years = 0
    while True:
        found = False  # 빙산이 다 녹았는지 확인
        q = deque([])

        for i in range(1, N-1):
            for j in range(1, M-1):
                if arr[i][j] != 0:
                    found = True
                    ice = 0
                    for di, dj in direct:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                            ice += 1
                    q.append((i, j, ice))  # 빙산의 위치와 주변 0의 개수 q에 삽입
        
        while q:
            r, c, ice = q.popleft()
            if arr[r][c] - ice < 0:
                arr[r][c] = 0
            else:
                arr[r][c] -= ice
        
        years += 1
        
        # 빙산이 두 덩어리 이상인지 확인
        if check():
            return years

        # 빙산이 다 녹았는데도 두 개 이상이 아니라면 0 리턴
        if not found:
            return 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
print(bfs())