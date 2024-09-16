# 3584. 가장 가까운 공통 조상
import sys
input = sys.stdin.readline

# def Find(x):
#     # if x == p[x]:
#     #     return x
#     # return Find(p[x])
#     if x != p[x]:
#         p[x] = Find(p[x])
#     return p[x]

# def Union(x, y):
#     px = Find(x)
#     py = Find(y)

#     if px != py:
#         if rank[px] < rank[py]:
#             p[px] = py
#         elif rank[px] > rank[py]:
#             p[py] = px
#         else:
#             p[px] = py
#             rank[py] += 1

T = int(input())
for _ in range(T):
    N = int(input())

    parent = [[i] for i in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B].append(A)
    
    n1, n2 = map(int, input().split())
    print(parent)

    p1 = []
    p2 = []

    
    # for i in parent[n1]:




    # edges = []
    # for _ in range(N-1):
    #     A, B = map(int, input().split())
    #     edges.append((A, B))
    
    # p = [i for i in range(N+1)]
    # rank = [0] * (N+1)
    # for s, e in edges:
    #     if Find(s) != Find(e):
    #         Union(s, e)

    # n1, n2 = map(int, input().split())
    
    # print(p)
    # print(Find(n1))
    # print(Find(n2))
