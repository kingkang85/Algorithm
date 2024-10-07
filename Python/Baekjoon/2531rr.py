# 2531. 회전 초밥
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dishes = []
for _ in range(N):
    dishes.append(int(input()))