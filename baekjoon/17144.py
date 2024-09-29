# 17144. 미세먼지 안녕!
'''
1. 공기청정기 위치 저장

2. 미세먼지 확산
- 현재 위치에서 갈 수 있는 다음 위치 저장
    - 다음 위치, 확산 양 저장
    - 현재 위치에서 미세먼지 양 빼기

3. 공기청정기 작동
- 첫 번째 공기청정기는 반시계
- 두 번째 공기청정기는 시계
- 공기청정기를 만나면 0
'''
import sys
input = sys.stdin.readline

# 공기청정기 찾기
def FindCleaner():
    result = []
    for i in range(R):
        if arr[i][0] == -1:
            result.append(i)
            if len(result) == 2:
                return result

# 미세먼지 확산
def Dust():
    next_pos = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        cnt += 1
                        next_pos.append((ni, nj, arr[i][j]//5))
                arr[i][j] = arr[i][j] - arr[i][j] // 5 * cnt
                
    for r, c, dust in next_pos:
        arr[r][c] += dust

# 공기청정기 작동
def Clean():
    top, bottom = cleaners
    # 위쪽 공기청정기
    for i in range(top-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for j in range(C-1):
        arr[0][j] = arr[0][j+1]
    for i in range(top):
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 1, -1):
        arr[top][j] = arr[top][j-1]
    arr[top][1] = 0

    # 아래쪽 공기청정기
    for i in range(bottom+1, R-1):
        arr[i][0] = arr[i+1][0]
    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, bottom, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 1, -1):
        arr[bottom][j] = arr[bottom][j-1]
    arr[bottom][1] = 0
            

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

cleaners = FindCleaner()
for _ in range(T):
    Dust()
    Clean()

total = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != 0 and arr[i][j] != -1:
            total += arr[i][j]

print(total)