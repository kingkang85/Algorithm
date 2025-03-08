# 23747. 와드
from collections import deque
import sys
input = sys.stdin.readline

def bfs(str, stc):
    if vision[str][stc] == ".":
        return
    
    q = deque([(str, stc)])
    vision[str][stc] = "."
    area = arr[str][stc]
    
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and vision[nr][nc] == "#" and arr[nr][nc] == area:
                q.append((nr, nc))
                vision[nr][nc] = "."


R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]
hr, hc = map(int, input().split())
path = input().strip()

direction = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
vision = [["#"] * C for _ in range(R)]

hr -= 1
hc -= 1
for p in path:
    if p == "W":
        bfs(hr, hc)
    else:
        hr += direction[p][0]
        hc += direction[p][1]

vision[hr][hc] = "."
for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
    nr, nc = hr + dr, hc + dc
    if 0 <= nr < R and 0 <= nc < C:
        vision[nr][nc] = "."

for row in vision:
    print("".join(row))