# 2206. 벽 부수고 이동하기
import copy

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    q = []
    q.append([i, j])
    visited[i][j] == 1

    cnt = 0
    while q:
        ti, tj = q.pop(0)
        cnt += 1
        if ti == N-1 and tj == M-1:
            return cnt

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = ti + di
            nj = tj + dj

            if 0 <= ni < N and 0 <= nj < M and tmp[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return -1

N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]

wall_lst = [[0, 0]]
for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            wall_lst.append([i, j])


MinV = N * M
for wall in wall_lst:
    tmp = copy.deepcopy(map)
    tmp[wall[0]][wall[1]] = 0
    result = bfs(0, 0)

    if result != -1:
        if MinV > result:
            MinV = result

if MinV == N * M:
    print(-1)
else:
    print(MinV)



