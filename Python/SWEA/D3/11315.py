# 11315. 오목 판정
def f(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0

                ni, nj = i, j  # 시작 인덱스
                while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:  # 5개이면 오목
                        return 'YES'
                    ni += di[k]  # 같은 방향으로 전진!
                    nj += dj[k]

    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]

    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]

    print(f'#{tc} {f(N)}')