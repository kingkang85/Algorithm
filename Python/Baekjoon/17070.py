# 17070. 파이프 옮기기 1
'''
dp 이용
- 현재 위치가 파이프의 끝이라고 생각!! 파이프의 방향에 따라..
1. 방향이 가로인 경우 : 이전 가로 방향 + 이전 대각선 방향
2. 방향이 세로인 경우 : 이전 세로 방향 + 이전 대각선 방향
3. 방향이 대각선인 경우 : 이전 가로 방향 + 이전 세로 방향 + 이전 대각선 방향
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]  # 방향, 행, 열 순서

# 0행은 항상 한 가지
dp[0][0][1] = 1
for i in range(2, N):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

# 0행은 위에서 처리했으므로 제외
for i in range(1, N):
    # 0열에는 파이프의 끝이 올 수 없으므로 제외
    for j in range(1, N):
        # 파이프의 방향이 가로(0), 세로(1)인 경우
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

        # 파이프의 방향이 대각선(2)인 경우
        if arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i-1][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]


# 가로, 세로, 대각선의 경우를 모두 더한 결과
result = sum(dp[i][N-1][N-1] for i in range(3))
print(result)