# 5656. [모의 SW 역량테스트] 벽돌 깨기
from collections import deque
def Crush(cnt, midSum, arr):
    global total_bricks, maxV
    # 벽돌을 다 깨면 return
    if midSum == total_bricks:
        maxV = midSum
        return
    
    # 구슬을 다 쏘면 return
    if cnt == N:
        maxV = max(maxV, midSum)
        return
    
    # 열마다 탐색
    for col in range(W):
        tmp = [r[:] for r in arr]
        stack = deque()
        crushed_bricks = 0
        
        for row in range(H):
            if tmp[row][col]:  # 시작 위치
                stack.append([row, col])
                break
        
        while stack:
            r, c = stack.pop()
            if not tmp[r][c]:  # 0이 된 벽돌들 제외
                continue

            # 현재 벽돌을 기준으로 상하좌우 확인
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nr, nc = r, c
                for _ in range(tmp[r][c] - 1):
                    nr += dr
                    nc += dc

                    # 유효한 벽돌이라면 stack에 추가
                    if 0 <= nr < H and 0 <= nc < W:
                        stack.append([nr, nc])
            
            tmp[r][c] = 0  # 현재 벽돌 부수기
            crushed_bricks += 1
            
        # 0이 된 벽돌 제거
        for j in range(W):
            idx = H - 1 
            for i in range(H - 1, -1, -1):
                if not tmp[i][j]:
                    continue
                tmp[idx][j], tmp[i][j] = tmp[i][j], tmp[idx][j]
                idx -= 1

        Crush(cnt + 1, midSum + crushed_bricks, tmp)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    
    total_bricks = 0  # 전체 벽돌 개수
    for i in range(H):
        for j in range(W):
            if bricks[i][j]:
                total_bricks += 1
    
    maxV = 0  # 최대로 깨트린 벽돌 개수
    Crush(0, 0, bricks)
    result = total_bricks - maxV
    print(f'#{tc} {result}')
    