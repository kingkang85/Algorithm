# 1446. 지름길
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort()

dist = [i for i in range(D+1)]  # 각 지점까지의 최단 거리
for i in range(D+1):
    # 전보다 1만큼 더 가는 경우
    if i > 0:
        dist[i] = min(dist[i], dist[i-1] + 1)
    
    # 현재 지점에서 시작하는 지름길이 있는지 확인
    for start, end, length in shortcuts:
        if start == i and end <= D:
            dist[end] = min(dist[end], dist[start] + length)

print(dist[D])