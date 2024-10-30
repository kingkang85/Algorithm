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
        if 0 <= ni < R and 0 <= nj < C:
            dfs(ni, nj, cnt + 1)
            used.remove(arr[ni][nj])

R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]

maxV = 0
used = set()
dfs(0, 0, 1)
print(maxV)