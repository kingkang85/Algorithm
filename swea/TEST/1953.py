# 1953. [모의 SW 역량테스트] 탈주범 검거
'''
bfs 이용
1. 시작 위치 R, C 를 넘겨준다.
2. 해당 번호에 따라 갈 수 있는 방향 중 하나를 선택
3. 이를 L시간이 될 때까지 반복 (단, 1시간부터 시작)
4. 방문한 맨홀 개수 출력
'''
from collections import deque

import sys
sys.stdin = open('sample_input.txt','r')
def bfs(sti, stj):
    global cnt
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((sti, stj, 1))  # 시작 행, 시작 열, 시간
    visited[sti][stj] = 1

    while q:
        i, j, time = q.popleft()
        if time == L:  # L시간이 되면 종료
            return cnt
        
        num = arr[i][j]
        # 맨홀의 번호에 해당하는 방향 반복
        for di, dj in turnel_type[num]:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] != 0:
                # (주의) 새로 간 맨홀이 이전 맨홀과 연결되어 있는지 확인
                for dr, dc in turnel_type[arr[ni][nj]]:
                    newi, newj = ni + dr, nj + dc
                    # 전 맨홀과 연결되어 있을 때
                    if newi == i and newj == j:
                        q.append((ni, nj, time + 1))  # q에 추가
                        visited[ni][nj] = 1           # 방문 표시
                        cnt += 1                      # 개수 추가


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 터널 번호에 해당하는 방향 저장
    turnel_type = {1:direct, 2:[direct[0], direct[2]], 3:[direct[1], direct[3]], 4:[direct[0], direct[1]],
                  5:[direct[1], direct[2]], 6:[direct[2], direct[3]], 7:[direct[0], direct[3]]}
    
    cnt = 1  # 맨홀 개수 (시작 맨홀부터 세야 하므로 1로 초기화)
    bfs(R, C)
    print(f'#{tc} {cnt}')