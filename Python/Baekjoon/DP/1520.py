# 1520. 내리막 길
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
    # 도착하면 경로 하나 추가
    if r == M-1 and c == N-1:
        return 1
    
    # 이미 방문한 곳이라면 그 곳을 출발점으로 하는 경로의 수 리턴
    if dp[r][c] != -1:
        return dp[r][c]
    
    cnt = 0
    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] < arr[r][c]:
           cnt += dfs(nr, nc)

    dp[r][c] = cnt
    return dp[r][c]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
print(dfs(0, 0))  