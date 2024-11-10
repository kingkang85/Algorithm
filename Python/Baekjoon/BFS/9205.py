# 9205. 맥주 마시면서 걸어가기
from collections import deque
import sys
input = sys.stdin.readline

# 맥주 20병으로 갈 수 있는지 확인
def can_go(nowr, nowc, nextr, nextc):
    return abs(nowr - nextr) + abs(nowc - nextc) <= 1000

def bfs(str, stc):
    q = deque([(str, stc)])
    visited.add((str, stc))

    while q:
        r, c = q.popleft()
        
        # 페스티벌에 도착하면 'happy' 리턴
        if r == route[-1][0] and c == route[-1][1]:
            return 'happy'
        
        for nr, nc in route:
            # 방문한 적이 없고 갈 수 있다면 q에 추가
            if (nr, nc) not in visited and can_go(r, c, nr, nc):
                q.append((nr, nc))
                visited.add((nr, nc))
    
    return 'sad'
                
t = int(input())
for _ in range(t):
    n = int(input())
    route = [list(map(int, input().split())) for _ in range(n+2)]
    visited = set()
    print(bfs(route[0][0], route[0][1]))  # 집에서 출발