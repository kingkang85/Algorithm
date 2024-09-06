# 5656. [모의 SW 역량테스트] 벽돌 깨기
def Crush(idx):
    for i in range(H):
        if bricks[i][idx] == 1:
            st = i

    for i in range(st, H):
        if bricks[st][idx] > 1:
            for k in range(bricks[st][idx]-1):
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    pass


def get_comb(lev):
    if lev == N:
        for c_idx in path:
            Crush(c_idx)  # 이걸 하나만 보내는 게 맞나??
        return
    
    for i in range(W):
        path.append(i)
        get_comb(lev + 1)
        path.pop()

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    path = []
    get_comb(0)

    