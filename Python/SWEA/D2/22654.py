# 22654. 차윤이의 RC카
def FindStart():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                return i, j

def MoveCar():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    d = 0
    r, c = sti, stj
    for move in commands:
        if move == 'R':
            d = (d + 1) % 4
        elif move == 'L':
            d = (d - 1) % 4
        else:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 'T':
                r, c = nr, nc

    return 1 if arr[r][c] == 'Y' else 0
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    Q = int(input())

    sti, stj = FindStart()
    result = []
    for _ in range(Q):
        _, commands = input().split()
        result.append(MoveCar())

    print(f'#{tc}', ' '.join(map(str, result)))