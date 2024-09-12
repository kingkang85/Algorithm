# 17472. 다리 만들기 2
from collections import deque
# 섬 찾는 함수
def FindIsland():
    global num
    q = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 1이고 방문한 적 없는 곳에서 시작
            if arr[i][j] == 1 and visited[i][j] == 0:
                num += 1
                arr[i][j] = num
                q.append((i, j))
                visited[i][j] = 1

            while q:
                i, j = q.popleft()
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        arr[ni][nj] = num  # 섬 번호 부여
                        q.append((ni, nj))
                        visited[ni][nj] = 1

# 다리 건설하는 함수
def Bridge():
    island = set()
    for _ in range(num):
        for i in range(N):
            for j in range(M):
                cnt = 0
                if arr[i][j] == num:


                    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                        r, c = i, j
                        while True:
                            nr, nc = r + dr, c + dc
                            cnt += 1
                            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == num:
                                break

                            if arr[nr][nc] > num and cnt >= 2:
                                island.add((num, arr[nr][nc], cnt))
                                break

                            r, c = nr, nc

    return island



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
num = 0  # 섬의 개수
FindIsland()
print(Bridge())



