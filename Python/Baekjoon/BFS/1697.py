# 1697. 숨바꼭질
from collections import deque
import sys
input = sys.stdin.readline

def Hiding():
    q = deque([(N, 0)])  # 현재 위치, 시간
    visited = set([N])

    while q:
        loc, time = q.popleft()

        # 동생을 찾으면 시간 리턴
        if loc == K:
            return time
        
        # +1, -1, *2만큼 움직일 수 있음
        for nloc in [loc + 1, loc - 1, loc * 2]:
            if 0 <= nloc <= 100000 and nloc not in visited:
                q.append((nloc, time + 1))
                visited.add(nloc)

N, K = map(int, input().split())
print(Hiding())