# 1949. [모의 SW 역량테스트] 등산로 조성
def dfs(r, c, cnt, isCut, curV):
    global result   
    if result < cnt:
        result = cnt

    visited[r][c] = True
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj = r + di, c + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if arr[ni][nj] < curV:  # 작은 곳으로 가보렴..
                dfs(ni, nj, cnt + 1, isCut, arr[ni][nj])
            
            else:  # 큰 곳으로 가보렴..
                if not isCut and arr[ni][nj] - K < arr[r][c]:
                    dfs(ni, nj, cnt + 1, True, arr[r][c] - 1)
    visited[r][c] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = max(map(max, arr))
    
    # 시작 위치
    highest = []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == maxV:
                highest.append((row, col))

    result = 0
    for row, col in highest:
        visited = [[0] * N for _ in range(N)]
        dfs(row, col, 1, False, arr[row][col])

    print(f'#{tc} {result}')