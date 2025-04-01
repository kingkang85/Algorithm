# 9657. 돌 게임 3
'''
현재 N개의 돌이 있고 내 차례라고 하면,
1개, 3개, 또는 4개의 돌을 가져갈 수 있음.
내가 x개의 돌을 가져가면 (N-x)개의 돌이 남고 상대방 차례가 됨.

=> N-x 중 하나라도 0이면 상근이가 이길 수밖에 없음
'''
import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 1, 0, 1, 1]

for i in range(5, N+1):
    if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
        dp.append(1)
    else:
        dp.append(0)

if dp[N] == 1:
    print("SK")
else:
    print("CY")