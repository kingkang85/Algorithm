# 3584. 가장 가까운 공통 조상
# LCA (Lowest Common Ancestor) Algorithm
import sys
input = sys.stdin.readline

# 해당 노드의 조상을 찾는 함수
def find_ancestors(node):
    ancestors = [node]  # 자기 자신 포함
    while p[node]:
        node = p[node]
        ancestors.append(node)
    return ancestors

# 두 노드의 공통 조상을 찾는 함수
def lca(n1, n2):
    a1 = find_ancestors(n1)
    a2 = find_ancestors(n2)

    # 첫 번째 노드의 조상 리스트 순회
    for data in a1:
        if data in a2:   # 두 번째 노드의 조상 리스트에도 존재하는 첫 번째 조상
            return data  # => 가장 가까운 공통 조상


T = int(input())
for _ in range(T):
    N = int(input())

    p = [0] * (N+1)  # 부모 저장
    for _ in range(N-1):
        A, B = map(int, input().split())
        p[B] = A

    n1, n2 = map(int, input().split())
    print(lca(n1, n2))