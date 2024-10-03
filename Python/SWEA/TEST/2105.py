# 2105. [모의 SW 역량테스트] 디저트 카페
def dfs(i, j, sti, stj, direct, visited):
    global maxV
    if i < 0 or i >= N or j < 0 or j >= N:
        return

    if direct == 3 and len(visited) <= maxV // 2:
        return

    # 모든 방향을 탐색하고 시작위치와 같아질 때 중단
    if direct == 3 and i == sti and j == stj:
        maxV = max(maxV, len(visited))
        return

    # 이미 있어?! 중단
    if dessert[i][j] in visited:
        return

    visited.add(dessert[i][j])
    ni, nj = i + di[direct], j + dj[direct]
    dfs(ni, nj, sti, stj, direct, visited)  # 방향 바꾸지마
    if direct < 3:
        dfs(ni, nj, sti, stj, direct+1, visited)  # 방향 바꿔
    visited.remove(dessert[i][j])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 1, -1]
    dj = [1, 1, -1, -1]

    maxV = -1
    for i in range(N-1):
        for j in range(N-1):
            dfs(i, j, i, j, 0, set())

    print(f'#{tc} {maxV}')