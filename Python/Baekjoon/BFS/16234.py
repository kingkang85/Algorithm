# 16234. 인구 이동
from collections import deque
import sys
input = sys.stdin.readline

# 연합국 탐색하는 함수
def bfs(sti, stj):
    q = deque([(sti, stj)])
    visited[sti][stj] = 1
    temp = [(sti, stj)]
    sumV = arr[sti][stj]  # 연합 인구 수
    cnt = 1  # 연합국 수

    while q:
        r, c = q.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                diff = abs(arr[r][c] - arr[nr][nc])

                if L <= diff <= R:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    temp.append((nr, nc))
                    sumV += arr[nr][nc]
                    cnt += 1

    # 연합국이 있을 때
    if cnt > 1:
        ppl = sumV // cnt  # 연합을 이루는 각 나라 인구 수
        for r, c in temp:
            arr[r][c] = ppl  # 연합국마다 값 저장
        return True
    
    return False


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

day = 0  # 인구 이동 횟수
while True:
    found = False  # 국경선이 열렸는지 확인
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bfs(i, j):
                found = True

    # 어느 나라에서도 국경선이 열리지 않았다면 종료
    if not found:
        break
    day += 1  # 하루 증가

print(day)            