# 11559. Puyo Puyo
# 8:20
'''
1. 배열을 탐색하면서 .이 아닌 것을 찾는다.
2. 해당 시작점의 문자와 같은 것이 아닐 때까지 탐색하면서 인덱스 추출
    - 단 개수가 4개 이상이어야 함
3. 추출된 인덱스들을 동시에 .으로 바꿈
4. 배열 바꾸는 함수 쓰기
5. 위 과정을 반복하며 카운트 세기

배열 바꾸는 함수!! (열 탐색)
- 밑에서부터 올라가면서 개수를 세며 .인 것을 확인
    - .이 아닌 것을 만나면 해당 요소를 개수만큼 밑으로 내림.
    - 다 .이면 pass
'''
from collections import deque
import sys
input = sys.stdin.readline

def change_field():
    for j in range(6):
        row = 11
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                if row != i:
                    field[row][j], field[i][j] = field[i][j], field[row][j]
                row -= 1

def bfs(str, stc, color):
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
        
    if len(chain) >= 4:
        return chain
    
    return False

field = [list(input().strip()) for _ in range(12)]

result = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    found = False
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and visited[i][j] == 0:
                chain = bfs(i, j, field[i][j])
                if chain:
                    found = True
                    for r, c in chain:
                        field[r][c] = '.'
    
    if not found:
        break

    change_field()
    result += 1

print(result)