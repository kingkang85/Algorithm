# 17135. 캐슬 디펜스
'''
먼저 시작점 3개를 찾는다!!
1. 시작점이 1이면 카운트 하나 업
2. bfs로 탐색하며 1을 만나면 카운트 하나 업
3. 거리가 D-1이 되면 종료
'''

from collections import deque
import sys
input = sys.stdin.readline

def attack(lev, st):
    if lev == 3:
        # 여기 bfs 채워라.
        return

    for i in range(st, M):
        if not used[i]:
            starts.append((N-1, i))
            used[i] = 1
            attack(lev+1, i+1)
            starts.pop()
            used[i] = 0


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starts = []
used = [0] * M
attack(0, 0)