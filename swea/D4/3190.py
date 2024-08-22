# 3190. 뱀
def Snake(i, j):
    q = []  # 뱀이 있는 곳의 인덱스
    q.append([i, j])  # 시작 인덱스 => (0, 0)
    board[i][j] = 1
    time = 0

    # 방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0

    while True:
        # 해당 시간이 되면 방향을 바꿈
        if time in X_lst:
            idx = X_lst.index(time)
            if D_lst[idx] == 'D':  # 오른쪽
                k = (k+1) % 4
            else:  # 왼쪽
                k = (k+3) % 4 

        # 뱀의 새로운 머리
        ni, nj = i + di[k], j + dj[k]
        time += 1

        # 벽을 만나거나 자기 자신과 부딪히면 time 리턴
        if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] == 1:
            return time

        # 사과가 없다면 꼬리를 pop하고 board를 0으로 바꿈
        if q and board[ni][nj] == 0:
            ti, tj = q.pop(0)
            board[ti][tj] = 0
        
        # 새로운 머리에 1하고 뱀에 append
        board[ni][nj] = 1
        q.append([ni, nj])     
        i += di[k]
        j += dj[k]
           

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]  # 보드판

for _ in range(K):
    r, c = map(int, input().split())  # 사과의 위치
    board[r-1][c-1] = 2  # 사과 => 2

X_lst = []  # 방향 변환 시간
D_lst = []  # 변환 방향
S = int(input())
for _ in range(S):
    X, D = input().split()
    X_lst.append(int(X))
    D_lst.append(D)

print(Snake(0, 0))