# 3055. 탈출
'''
1. 물이 있는 칸을 모아서 상하좌우 물 채우기
    - 비버굴이 아니고 바위도 아닌 칸으로 갈 수 있음
2. 고슴도치가 이제 이동!
    - 물이 아니고 바위도 아닌 칸으로 갈 수 있음
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and arr[nr][nc] == '.':


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

q = deque()
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            q.append((i, j, '*'))
            visited[i][j] = 1
        elif arr[i][j] == 'S':
            hog = (i, j)
            visited[i][j] = 1
q.append(hog, 'S')

