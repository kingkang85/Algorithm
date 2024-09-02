# 21608. 상어 초등학교
def Shark(i, j):
    global cnt
    for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == 0:
            cnt += 1
    

N = int(input())
for _ in range(N*N):
    arr = list(map(int, input().split()))
    student = arr[0]
    wish = arr[1:]

    room = [[0] * N for _ in range(N)]

    Max = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            Shark(i, j)
            if Max < cnt:
                Max = cnt
                row, col = i, j

    room[row][col] = student
    print(room)

