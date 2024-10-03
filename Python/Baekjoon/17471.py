# 17471. 게리맨더링
N = int(input())  # 구역의 개수
population = list(map(int, input().split()))

graph = []
for _ in range(N):
    info = list(map(int, input().split()))
