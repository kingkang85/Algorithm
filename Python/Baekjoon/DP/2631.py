# 2631. 줄 세우기
import sys
input = sys.stdin.readline

N = int(input())
childs = []
for _ in range(N):
    childs.append(int(input()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if childs[i] > childs[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(N - max(dp))