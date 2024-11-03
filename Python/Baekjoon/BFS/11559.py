# 11559. Puyo Puyo
from collections import deque
import sys
input = sys.stdin.readline

# 중력 작용
def change_field():
    for j in range(6):
        row = 11
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                if row != i:
                    field[row][j], field[i][j] = field[i][j], field[row][j]
                row -= 1

def bfs(str, stc, color):  # 시작 위치와 해당 색깔
    q = deque([(str, stc)])
    visited[str][stc] = 1
    chain = [(str, stc)]
    
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 12 and 0 <= nc < 6 and visited[nr][nc] == 0 and field[nr][nc] == color:
                q.append((nr, nc))
                chain.append((nr, nc))
                visited[nr][nc] = 1
    
    # 4개 이상 모일 경우
    if len(chain) >= 4:
        return chain
    
    # 4개 미만은 False
    return False

field = [list(input().strip()) for _ in range(12)]

result = 0  # 연쇄 수
while True:
    visited = [[0] * 6 for _ in range(12)]
    found = False
    for i in range(12):
        for j in range(6):
            # 색깔 뿌요이고 방문 안 한 곳이라면 bfs 시작
            if field[i][j] != '.' and visited[i][j] == 0:
                chain = bfs(i, j, field[i][j])
                if chain:
                    found = True  # 연쇄가 일어나면 True
                    for r, c in chain:
                        field[r][c] = '.'
    
    # 게임 종료
    if not found:
        break
    
    change_field()
    result += 1

print(result)