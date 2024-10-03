# 12712. 파리퇴치3
# 주어진 방향으로 죽인 파리 총합을 구하는 함수
def KillFlies(direction):
    kill = fly[i][j]
    for k in range(1, M):
        for di, dj in direction:
            ni = i + di * k
            nj = j + dj * k

            if 0 <= ni < N and 0 <= nj < N:
                kill += fly[ni][nj]
    
    return kill


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    MaxV = 0
    for i in range(N):
        for j in range(N):
            # + 방향
            result1 = KillFlies([[0, 1], [1, 0], [0, -1], [-1, 0]])

            # x 방향
            result2 = KillFlies([[1, 1], [1, -1], [-1, -1], [-1, 1]])

            # 최댓값 찾기
            if MaxV < max(result1, result2):
                MaxV = max(result1, result2)

    print(f'#{tc} {MaxV}')
