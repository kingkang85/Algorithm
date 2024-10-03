# 14500. 테트로미노
# n: 사각형 개수, midSum: 누적합, path: 선택한 위치 리스트
def dfs(n, midSum, path):
    global result
    # 가지치기: 남은 사각형이 모두 maxV라 해도 result보다 작으면 중단
    if midSum + (4 - n) * maxV <= result:
        return
    
    # 테트로미노가 완성되면 최댓값 확인
    if n == 4:
        result = max(result, midSum)
        return
    
    # path에 저장된 인덱스 번호 이용
    for i, j in path:
        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 1  # 방문 표시
                dfs(n + 1, midSum + arr[ni][nj], path + [(ni, nj)])
                visited[ni][nj] = 0  # 복원


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maxV = max(map(max, arr))  # 배열의 최댓값 (가지치기를 위해 구해놓자.)

result = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1  # 방문 표시
        dfs(1, arr[i][j], [(i, j)])

print(result)


###################################################################################################
# 시초 코드
# def TetCheck(lst):
#     row, col = lst[0][0], lst[0][1]
#     new_lst = [[nrow - row, ncol - col] for nrow, ncol in lst]

#     check = [
#         [[0, 0], [0, 1], [0, 2], [0, 3]],
#         [[0, 0], [1, 0], [2, 0], [3, 0]],
#         [[0, 0], [0, 1], [1, 0], [1, 1]],
#         [[0, 0], [1, 0], [2, 0], [2, 1]],
#         [[0, 0], [1, 0], [2, -1], [2, 0]],
#         [[0, 0], [0, 1], [1, 0], [2, 0]],
#         [[0, 0], [0, 1], [1, 1], [2, 1]],
#         [[0, 0], [1, -2], [1, -1], [1, 0]],
#         [[0, 0], [1, 0], [1, 1], [1, 2]],
#         [[0, 0], [0, 1], [0, 2], [1, 2]],
#         [[0, 0], [0, 1], [0, 2], [1, 0]],
#         [[0, 0], [1, 0], [1, 1], [2, 1]],
#         [[0, 0], [1, -1], [1, 0], [2, -1]],
#         [[0, 0], [0, 1], [1, -1], [1, 0]],
#         [[0, 0], [0, 1], [1, 1], [1, 2]],
#         [[0, 0], [0, 1], [0, 2], [1, 1]],
#         [[0, 0], [1, -1], [1, 0], [1, 1]],
#         [[0, 0], [1, 0], [1, 1], [2, 0]],
#         [[0, 0], [1, -1], [1, 0], [2, 0]],
#         ]
    
#     if new_lst in check:
#         return True
    
#     return False


# def get_comb(lev, start):
#     global maxV
#     if lev == 4:
#         sumV = 0
#         if TetCheck(squares):
#             for s in squares:
#                 sumV += arr[s[0]][s[1]]

#         if maxV < sumV:
#             maxV = sumV
#         return
    
#     # 2차원 배열을 1차원으로 쭈욱 펼침
#     for idx in range(start + 1, N * M):
#         i, j = idx // M, idx % M  # 행 인덱스는 열 개수로 나눈 몫
#         squares.append([i, j])    # 열 인덱스는 열 개수로 나눈 나머지
#         get_comb(lev + 1, idx)
#         squares.pop()

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# squares = []
# maxV = 0
# get_comb(0, -1)
# print(maxV)

###############################################trash####################################################
# sumV = 0
# for i in range(3):
#     if abs(squares[i+1][0] - squares[i][0] + squares[i+1][1] - squares[i][1]) != 1:
#         break
#     sumV += arr[squares[i][0]][squares[i][1]]

#     # 뻐큐 모양은 따로 처리..
#     if squares[1][0] == squares[2][0] == squares[3][0] and squares[2][1] - squares[0][1] == 1:
#         pass
#     if squares[0][0] == squares[1][0] == squares[2][0] and squares[3][1] - squares[1][1] == 1:
#         pass
#     if squares[0][1] == squares[1][1] == squares[3][1] and squares[2][0] - squares[1][0] == 1:
#         pass
#     if squares[0][1] == squares[2][1] == squares[3][1] and squares[2][0] - squares[1][0] == 1:
#         pass

# sumV += arr[squares[-1][0]][squares[-1][1]]

# if maxV < sumV:
#     maxV = sumV