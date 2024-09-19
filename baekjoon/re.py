# 2559. 수열
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tmp = list(map(int, input().split()))

sumV = maxV = st = 0
for i in range(0, N-K+1):
    for j in range(st, i+K):
        sumV += tmp[j]
    
    if maxV < sumV:
        maxV = sumV
    
    sumV -= tmp[i]
    st += 1

print(maxV)
    