# 17472. 다리 만들기 2
from collections import deque, defaultdict
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
                island[num].append((i, j))

            while q:
                i, j = q.popleft()
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        arr[ni][nj] = num  # 섬 번호 부여
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        island[num].append((ni, nj))


# 다리 건설하는 함수
def Bridge():
    for k, v in island.items():
        for i, j in v:
            r, c = i, j
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                cnt = 0
                while True:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == k:
                        break

                    if arr[nr][nc] > k and cnt >= 2:
                        print(nr, nc)
                        edges.add((k, arr[nr][nc], cnt))
                        break
                    cnt += 1
                    r, c = nr, nc
    
    

def Find(x):
    if x != p[x]:
        p[x] = Find(p[x])
    return p[x]

def Union(x, y):
    px = Find(x)
    py = Find(y)

    if px != py:
        if rank[px] < rank[py]:
            p[px] = py
        elif rank[px] > rank[py]:
            p[py] = px
        else:
            p[px] = py
            rank[py] += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

num = 0  # 섬 개수
island = defaultdict(list)
edges = set()
FindIsland()
print(arr)
Bridge()
print(edges)
p = [i for i in range(num+1)]
rank = [0] * (num+1)
ans = 0
for s, e, w in edges:
    if Find(s) != Find(e):
        Union(s, e)
        ans += w

print(ans)