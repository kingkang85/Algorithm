# 11437. LCA
'''
1. 모든 노드에 대한 깊이를 구한다.
2. 최소 공통 조상을 찾을 두 노드에 대하여
    - 두 노드의 깊이를 동일하게 만든다.
    - 부모가 같아질 때까지 거슬러 올라간다.
'''
import sys
from collections import deque
input = sys.stdin.readline

# 깊이 구하는 함수
def bfs(start):
    q = deque([(start, 0)])
    visited[start] = 1
    d[start] = 0

    while q:
        node, depth = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                p[next] = node
                d[next] = depth + 1
                visited[next] = 1
                q.append((next, depth + 1))

# 최소 공통 조상 찾는 함수
def lca(v1, v2):
    # 깊이 맞추기
    while d[v1] != d[v2]:
        if d[v1] > d[v2]:
            v1 = p[v1]
        else:
            v2 = p[v2]
    
    # 최소 공통 조상 찾기
    while v1 != v2:
        v1 = p[v1]
        v2 = p[v2]
    
    return v1


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

p = [0] * (N+1)
d = [0] * (N+1)
visited = [0] * (N+1)
bfs(1)

M = int(input())
for _ in range(M):
    v1, v2 = map(int, input().split())
    print(lca(v1, v2))