# 2573. 빙산
'''
시작 위치 찾기
이어졌는지 계속 확인해라. 2개 되는 순간 시간 리턴!
1. 0이 아닌 것과 상하좌우 0의 개수를 q에 삽입
2. pop하여 원래 배열에서 0의 개수를 빼고 0보다 작으면 그냥 0 넣어
'''
from collections import deque
import sys
input = sys.stdin.readline

def check():
    for i in range(1, N-1):
        for j in range(1, M-1):
            

    
    


def bfs():
    q = deque([])
    visited = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] != 0:
                cnt = 0
                for di, dj in direct:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        cnt += 1
                q.append((i, j, cnt, 0))
                visited[i][j] = 1
    
    while q:
        r, c, cnt, time = q.popleft()
        
        if arr[r][c] - cnt < 0:
            arr[r][c] = 0
        else:
            arr[r][c] -= cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]

bfs()