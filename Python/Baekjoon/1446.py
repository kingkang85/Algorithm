# 1446. 지름길
N, D = map(int, input().split())
distance = [0] * 10001
for _ in range(N):
    start, end, length = map(int, input().split())
