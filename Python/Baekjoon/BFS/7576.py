# 7576. 토마토
'''
1. 배열을 탐색하며 1인 곳들 찾기
2. 1의 상하좌우를 살피며 0인 것들을 찾고 방문 표시, 익히기
4. 위의 과정이 모두 끝나고 배열에 0이 남아있다면 -1 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    found = False
    q = deque()
    # 익은 토마토 (1) 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                found = True

            if arr[i][j] == 1:
                q.append((i, j, 0))  # 위치, 일수
                visited[i][j] = 1
    
    # 처음부터 모든 토마토가 익어있는 경우 0 출력
    if not found:
        return 0
    
    while q:
        r, c, days = q.popleft()
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 0:
                q.append((nr, nc, days + 1))
                visited[nr][nc] = 1
                arr[nr][nc] = 1
    
    # 토마토가 모두 익지는 못하는 경우 -1 출력
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    
    return days
    

M, N = map(int, input().split())  # 열, 행
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
print(bfs())