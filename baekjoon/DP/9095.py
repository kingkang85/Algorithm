# 9095. 1, 2, 3 더하기
'''
N은
N - 1에 1을 더하는 것
N - 2에 2을 더하는 것
N - 3에 3을 더하는 것
위 세 가지 경우를 모두 더하는 것과 같음
'''
import sys
input = sys.stdin.readline

T = int(input())
dp = [0, 1, 2, 4] + [0] * 7
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    N = int(input())
    print(dp[N])