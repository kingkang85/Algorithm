# 21610. 마법사 상어와 비바라기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]  # 초기 구름 위치

for _ in range(M):
    d, s = map(int, input().split())  # d: 방향, s: 이동 칸 수

    visited = [[0] * N for _ in range(N)]  # 구름 방문 표시할 배열
    magic = []  # 물복사버그 마법 쓸 위치 
    direct = [0, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

    # 구름 이동시키기
    for _ in range(len(clouds)):
        r, c = clouds.pop()
        nr = (r + direct[d][0] * s) % N
        nc = (c + direct[d][1] * s) % N

        arr[nr][nc] += 1  # 물의 양 1 증가
        visited[nr][nc] = 1  # 방문 표시
        magic.append((nr, nc))  # 물복사버그 마법 쓸 위치 저장

    # 물복사버그 마법 시전
    for i, j in magic:
        for k in [2, 4, 6, 8]:
            newi = i + direct[k][0]
            newj = j + direct[k][1]
            
            # 배열을 벗어나지 않고 물이 있으면 "원래의 위치"에 1 증가
            if 0 <= newi < N and 0 <= newj < N and arr[newi][newj] != 0:
                arr[i][j] += 1

    # 새로운 구름 위치 추가하기
    for i in range(N):
        for j in range(N):
            # 방문한 적이 없고 물의 양이 2 이상
            if visited[i][j] == 0 and arr[i][j] >= 2:
                clouds.append((i, j))
                arr[i][j] -= 2
    
# 물의 양의 합 구하기
sumV = 0
for i in range(N):
    for j in range(N):
        sumV += arr[i][j]

print(sumV)