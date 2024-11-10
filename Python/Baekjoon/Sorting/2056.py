# 2056. 작업
from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    q = deque()
    
    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    while q:
        now = q.popleft()
        
        for next in graph[now]:
            indegree[next] -= 1
            # 선행 작업 중 가장 오래 걸리는 시간으로 갱신
            dp[next] = max(dp[next], dp[now] + time[next])

            if indegree[next] == 0:
                q.append(next)
    
    return max(dp)

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)
dp = [0] * (N+1)  # dp[i] : i번 작업까지 완료하는데 걸리는 최소 시간

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    
    # 선행 관계 처리
    for x in data[2:]:
        graph[x].append(i)
        indegree[i] += 1

print(topology_sort())