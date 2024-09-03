# 21608. 상어 초등학교
def Shark(i, j):
    global cnt
    for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == 0:
            cnt += 1
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N*N)]
room = [[0] * N for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         for s in arr:
#             student = s[0]
#             wish = s[1:]

empty = N*N
for s in arr:
    student = s[0]
    wish = s[1:]
    
    Max = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            Shark(i, j)
            if Max < cnt:
                Max = cnt
                row, col = i, j
                room[row][col] = student
                empty -= 1

    # Max = 0
    # for i in range(N):
    #     for j in range(N):
    #         cnt = 0
    #         Shark(i, j)
    #         if Max < cnt:
    #             Max = cnt
    #             row, col = i, j

    # room[row][col] = student
    # print(room)

