# 15686. 치킨 배달
N, M = map(int, input().split())
city = [[-1] * (N+1)] + [[-1] + list(map(int, input().split())) for _ in range(N)]

chicken = []  # 치킨집
home = []  # 가정집
for i in range(N+1):
    for j in range(N+1):
        if city[i][j] == 1:
            home.append([i, j])

        elif city[i][j] == 2:
            chicken.append([i, j])

MinV = 10e5  # 도시의 치킨 거리 최솟값
cn = len(chicken)
# 치킨집 부분집합 찾기
for i in range(1 << cn):
    subset = []
    for j in range(cn):
        if i & (1 << j):
            subset.append(chicken[j])
    
    chicken_dist = 0
    # 길이가 M인 부분집합
    if len(subset) == M:
        for h in home:
            MinS = 10e5  # 집에서 M개의 치킨집 중 가장 짧은 거리
            for c in subset:
                store_dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
                if MinS > store_dist:
                    MinS = store_dist

            chicken_dist += MinS  # 각 부분집합의 도시 치킨 거리

        if MinV > chicken_dist:
            MinV = chicken_dist

print(MinV)

