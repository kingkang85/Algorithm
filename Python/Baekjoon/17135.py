# 17135. 캐슬 디펜스
'''
먼저 시작점 3개를 찾는다!!
1. 시작점이 1이면 카운트 하나 업
2. bfs로 탐색하며 1을 만나면 카운트 하나 업
3. 거리가 D-1이 되면 종료
'''

from collections import deque
import sys
input = sys.stdin.readline

# 게임이 끝났는지 확인하는 함수
def check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return False
    return True


def attack(lev, st):
    global maxCnt
    if lev == 3:
        cnt = 0
        visited = [[0] * M for _ in range(N-1)] + [[1] * M]
        q = deque()
        for str, stc in starts:
            q.append((str, stc, 0))

            if arr[str][stc] == 1:
                arr[str][stc] = 0
                cnt += 1

        while q:
            r, c, dist = q.popleft()

            if dist == D-1:
                break

            for dr, dc in [[-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    q.append((nr, nc, dist + 1))
                    visited[nr][nc] = 1
                    cnt += 1

        maxCnt = max(maxCnt, cnt)
        return

    for i in range(st, M):
        if not used[i]:
            starts.append((N-1, i))
            used[i] = 1
            attack(lev+1, i+1)
            starts.pop()
            used[i] = 0


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starts = []
used = [0] * M
maxCnt = 0
attack(0, 0)
print(maxCnt)