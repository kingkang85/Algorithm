# 2559. 수열
import sys
N, K = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

Max = -100*K  # 나올 수 있는 값 중 최솟값으로 설정
for i in range(0, N-K+1):
    sumV = sum(temp[i:i+K])

    # 최댓값 비교
    if Max < sumV:
        Max = sumV

print(Max)