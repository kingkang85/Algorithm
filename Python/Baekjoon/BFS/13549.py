# 13549. 숨바꼭질 3
from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, K):
    MAX_POS = 100000
    visited = [0] * (MAX_POS + 1)

    q = deque([(N, 0)])
    visited[N] = 1

    while q:
        pos, time = q.popleft()

        if pos == K:
            return time
        
        next_pos = pos * 2
        if 0 <= next_pos <= MAX_POS and visited[next_pos] == 0:
            q.appendleft((next_pos, time))
            visited[next_pos] = 1

        for next_pos in [pos - 1, pos + 1]:
            if 0 <= next_pos <= MAX_POS and visited[next_pos] == 0:
                q.append((next_pos, time + 1))
                visited[next_pos] = 1
    
    return -1

N, K = map(int, input().split())
print(bfs(N, K))