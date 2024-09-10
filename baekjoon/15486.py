# 15486. 퇴사 2
N = int(input())
sche = []
for _ in range(N):
    T, P = map(int, input().split())
    sche.append((T, P))

dp = [0] * (N+1)