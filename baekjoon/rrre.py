# 2667. 단지번호붙이기
def Home():
    visited = [[0] * N for _ in range(N)]
    q = []
    cpx_cnt = 0
    apart = []

    for i in range(N):
        for j in range(N):
            if map[i][j] == 1 and visited[i][j] == 0:
                cpx_cnt += 1
                sti, stj = i, j

                q.append([sti, stj])
                visited[sti][stj] = 1
                home_cnt = 1

                while q:
                    ti, tj = q.pop(0)
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        wi, wj = ti + di, tj + dj
                        if 0 <= wi < N and 0 <= wj < N and map[wi][wj] == 1 and visited[wi][wj] == 0:
                            q.append([wi, wj])
                            visited[wi][wj] = 1
                            home_cnt += 1
                apart.append(home_cnt)

    apart.sort()
    print(cpx_cnt)
    print(*apart, sep='\n')

    return

N = int(input())
map = [list(map(int, input())) for _ in range(N)]
Home()



##### 강사님의 힌트 ???? #####
# def BFS(i, j):
#     visited = [[0] * N for _ in range(N)]
#     q = []
#     q.append([i, j])
#     visited[i][j] = 1
#
#     home_cnt = 1
#     while q:
#         ti, tj = q.pop(0)
#         for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#             wi, wj = ti+di, tj+dj
#
#             if 0<= wi < N and 0<= wj < N and map[wi][wj] == 1 and visited[wi][wj] == 0:
#                 q.append([wi, wj])
#                 visited[wi][wj] = 1
#                 home_cnt += 1
#
#     return home_cnt
#
#
# N = int(input())
# map = [list(map(int, input())) for _ in range(N)]
#
# home_lst = []
# cpx_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if map[i][j] == 1:
#            cpx_cnt += 1
#            home_lst.append(BFS(i, j))
#
# print(cpx_cnt)
# print(*home_lst, sep='\n')
