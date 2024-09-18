# 11438. LCA 2
import sys
from math import log2
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 바로 위의 부모만 저장
def dfs(st, depth):
    visited[st] = 1
    d[st] = depth

    for next in tree[st]:
        if visited[next]:
            continue
        p[next][0] = st
        dfs(next, depth + 1)

# 모든 노드의 조상 저장
def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, N+1):
            p[j][i] = p[p[j][i-1]][i-1]

def lca(a, b):
    # 무조건 b의 깊이가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    
    # a와 b의 깊이 맞추기
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = p[b][i]
    
    if a == b:
        return a
    
    # 공통 조상 찾기
    for i in range(LOG - 1, -1, -1):
        if p[a][i] != p[b][i]:
            a = p[a][i]
            b = p[b][i]
    
    return p[a][0]


N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

LOG = int(log2(N)) + 1
p = [[0] * LOG for _ in range(N+1)]
d = [0] * (N+1)
visited = [0] * (N+1)
set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))