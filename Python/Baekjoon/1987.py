# 1987. 알파벳
import sys
input = sys.stdin.readline

def dfs(i, j, cnt):
    global maxV

    if arr[i][j] in used:
        maxV = max(maxV, cnt)
        return

    used.add(arr[i][j])
    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            used.add(arr[ni][nj])
            dfs(ni, nj, cnt + 1)
            visited[ni][nj] = 0

R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]

maxV = 0
visited = [[0] * C for _ in range(R)]
used = set()
dfs(0, 0, 1)
print(maxV)