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
                r, c = q.popleft()  # (주의) i, j로 쓰면 안 된다 ㅠ
                for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                        arr[nr][nc] = num  # 섬 번호 부여
                        q.append((nr, nc))
                        visited[nr][nc] = 1
                        island[num].append((nr, nc))


# 다리 건설하는 함수
def Bridge():
    edges = set()
    for k, v in island.items():
        for i, j in v:
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nr, nc = i + dr, j + dc
                length = 0

                while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != k:
                    if arr[nr][nc] != 0:
                        if length >= 2:
                            edges.add((k, arr[nr][nc], length))
                        break
                    length += 1
                    nr, nc = nr + dr, nc + dc
    
    return list(edges)
    
    
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
FindIsland()
edges = Bridge()

edges.sort(key = lambda x: x[2])

p = [i for i in range(num+1)]
rank = [0] * (num+1)
ans = 0
cnt = 0
for s, e, w in edges:
    if Find(s) != Find(e):
        Union(s, e)
        ans += w
        cnt += 1

# 섬이 모두 연결되었는지 확인 => 간선 수 == 노드 수 - 1
if cnt == num - 1:
    print(ans)
else:
    print(-1)