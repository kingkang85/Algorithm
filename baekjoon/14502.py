# 14502. 연구소
from itertools import combinations
import copy

def Virus(i, j):
    visited = [[0] * M for _ in range(N)]
    q = []
    q.append([i, j])
    visited[i][j] = 1

    while q:
        ti, tj = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi = ti + di
            wj = tj + dj

            if 0 <= wi < N and 0 <= wj < M and tmp[wi][wj] == 0 and visited[wi][wj] == 0:
                tmp[wi][wj] = 3
                q.append([wi, wj])
                visited[wi][wj] = 1
 

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

wall_lst = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            wall_lst.append([i, j])

MaxV = 0

for wall_lst in list(combinations(wall_lst, 3)):
    tmp = copy.deepcopy(lab)
    for wall in wall_lst:
        tmp[wall[0]][wall[1]] = 1
    
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                Virus(i, j)
                    
    safe = 0
    for row in tmp:
        safe += row.count(0)

    if MaxV < safe:
        MaxV = safe

print(MaxV)
