# 18428. 감시 피하기
import sys
input = sys.stdin.readline

# 감시를 피할 수 있는지 확인
def check():
    for r in range(N):
        for c in range(N):
            # 선생님의 상하좌우 확인
            if arr[r][c] == 'T':
                for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 'O':
                            break
                        elif arr[nr][nc] == 'S':
                            return False  # 학생 발각
                        nr += dr
                        nc += dc
    return True

def dfs(cnt):
    # 장애물 3개 설치 후 감시 체크
    if cnt == 3:
        return check()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                if dfs(cnt + 1):
                    return True
                arr[i][j] = 'X'
                
    return False

N = int(input())
arr = [input().split() for _ in range(N)]

if dfs(0):
    print('YES')
else:
    print('NO')