# 13460. 구슬 탈출 2
from collections import deque

# 시작 위치 찾는 함수
def FindStart():
    Rr = Rc = Br = Bc = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                Rr, Rc = i, j  # 빨간 구슬 위치  

            elif board[i][j] == 'B':
                Br, Bc = i, j  # 파란 구슬 위치

    return Rr, Rc, Br, Bc

# 구슬 움직이는 함수
def Move(r, c, dr, dc):
    cnt = 0  # 이동 칸 수
    # '#'(벽)이나 'O'(구멍) 만나기 전까지 계속 이동
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt  # 최종 위치와 이동 칸 수 반환

def bfs():
    q = deque()
    visited = set()
    ri, rj, bi, bj = FindStart()
    q.append((ri, rj, bi, bj, 0))  # 큐에 초기 상태 추가
    visited.add((ri, rj, bi, bj))  # 방문 표시

    while q:
        ri, rj, bi, bj, depth = q.popleft()

        if depth >= 10:  # 10번 넘어가면 실패
            break
        
        # 네 방향으로 기울이기
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            newri, newrj, rcnt = Move(ri, rj, dr, dc)  # 빨간 구슬 이동
            newbi, newbj, bcnt = Move(bi, bj, dr, dc)  # 파란 구슬 이동

            if board[newbi][newbj] == 'O':  # 파란 구슬이 구멍에 빠지면 실패
                continue

            if board[newri][newrj] == 'O':  # 빨간 구슬만 구멍에 빠지면 성공
                return depth + 1  # (주의) 원래의 depth에서 한 번 더 기울여서 구멍에 빠졌으므로 1 더해줘야함

            # 두 구슬이 만나면 이동 거리가 긴(늦게 도착한) 구슬을 한 칸 뒤로
            if newri == newbi and newrj == newbj:
                if rcnt > bcnt:
                    newri -= dr
                    newrj -= dc

                else:
                    newbi -= dr
                    newbj -= dc

            # 방문 안 한 곳이라면 큐에 추가하고 방문 표시
            if (newri, newrj, newbi, newbj) not in visited:
                q.append((newri, newrj, newbi, newbj, depth + 1))
                visited.add((newri, newrj, newbi, newbj))
    
    return -1

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
print(bfs())