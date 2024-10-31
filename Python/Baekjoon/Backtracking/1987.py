# 1987. 알파벳
import sys
input = sys.stdin.readline

def dfs(i, j, cnt):
    global maxV
    maxV = max(maxV, cnt)

    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and used[ord(arr[ni][nj]) - 65] == 0:
            used[ord(arr[ni][nj]) - 65] = 1
            dfs(ni, nj, cnt + 1)
            used[ord(arr[ni][nj]) - 65] = 0

R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]

maxV = 0
used = [0] * 26
used[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)
print(maxV)