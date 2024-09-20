# 2559. 수열
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tmp = list(map(int, input().split()))

result = [sum(tmp[:K])]

for i in range(N-K):
    ans = result[i] - tmp[i] + tmp[i+K]
    result.append(ans)

print(max(result))