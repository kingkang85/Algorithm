# 14567. 선수과목
from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    q = deque()
    result = [0] * (N+1)  # 각 과목별 최소 학기

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append((i, 1))
        
    while q:
        now, time = q.popleft()
        result[now] = time

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append((next, time+1))
    
    return result

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)  # 진입 차수

# 선행 관계 파악
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort()[1:])