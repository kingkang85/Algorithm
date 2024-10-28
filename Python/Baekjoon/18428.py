# 18428. 감시 피하기
'''
dfs
- 장애물 설치 갯수가 3개가 될 때까지 감시를 못 피했다면 NO return
- 장애물 설치 할 때마다 감시 피했는지 확인 => 피했다면 YES return

'''
import sys
input = sys.stdin.readline

def check():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'T':
                for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 'O':
                            break
                        elif arr[nr][nc] == 'S':
                            return False
                        nr += drS
                        nc += dc
    
    return True

def dfs(cnt):
    if cnt == 3 and check():
        return 'Yes'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                dfs(cnt + 1)
                arr[i][j] = 'X'

    return 'NO'
    
N = int(input())
arr = [input().split() for _ in range(N)]

dfs(0)
print('No')