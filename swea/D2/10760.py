# 10760. 우주선착륙2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0  # 예비 후보지 개수
    for i in range(N):
        for j in range(M):
            cnt = 0  # 착륙지 높이보다 낮은 지역 수
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] < arr[i][j]:
                        cnt += 1

            if cnt >= 4:  # 4곳 이상이면 예비 후보지 +1
                total += 1
    
    print(f'#{tc} {total}')