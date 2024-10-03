# 15486. 퇴사 2
import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
for i in range(1, N+1):
    T, P = map(int, input().split())
    
    dp[i] = max(dp[i], dp[i-1])  # 현재 날짜의 최댓값 갱신
    if i + T - 1 <= N:  # 퇴사 전까지 끝낼 수 있는지 확인
        dp[i+T-1] = max(dp[i+T-1], dp[i-1] + P)  # 상담 종료 날짜의 최댓값 갱신

print(dp[-1])