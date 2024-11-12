# 17471. 게리맨더링
from collections import deque
import sys
input = sys.stdin.readline

# 재귀를 이용한 조합 구현
def get_combs(arr, cnt, st=0):
    result = []
    if cnt == 0:
        return [[]]   
    
    for i in range(st, len(arr)):
        for rest in get_combs(arr, cnt - 1, i + 1):
            result.append([arr[i]] + rest)
    
    return result

# 노드끼리 연결되었는지 확인하는 함수
def check_connected(group):
    q = deque([group[0]])
    visited = set([group[0]])
    
    while q:
        now = q.popleft()

        for next in graph[now]:
            if next in group and next not in visited:
                q.append(next)
                visited.add(next)
    
    return len(visited) == len(group)  # 방문 노드 수와 원래 group 수가 같으면 True

N = int(input())  # 구역의 개수
population = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j in info[1:]:
        graph[i].append(j)

minV = 10**6
nodes = list(range(1, N+1))
found = False
for i in range(1, N//2 + 1):
    combs = get_combs(nodes, i)

    for group1 in combs:
        # group1에 포함되지 않는 나머지 노드들
        group2 = [node for node in nodes if node not in group1]

        if check_connected(group1) and check_connected(group2):
            found = True
            sum1 = sum(population[i] for i in group1)
            sum2 = sum(population[i] for i in group2)
            minV = min(minV, abs(sum1 - sum2))

# 두 선거구로 나누지 못한 경우 -1
if not found:
    minV = -1

print(minV)