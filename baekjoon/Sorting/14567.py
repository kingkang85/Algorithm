# 14567. 선수과목
import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque()
    result = [1] * (N+1)  # 최소 1학기로 초기화

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1

            # 현재 학기 + 1과 다음 학기 중 최댓값으로 갱신
            result[next] = max(result[next], result[now] + 1)

            if indegree[next] == 0:
                q.append(next)
    
    return result[1:]
    
    
N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

result = topology_sort()
print(*result)