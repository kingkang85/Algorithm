# 14413. 격자판 칠하기
def Coloring():
    # 모두 '?'이면 possible 
    for row in arr:
        if row != ['?'] * M:
            break
    else:
        return 'possible'
    
    # 모두 '?'는 아닌 경우
    while True:
        for i in range(N):
            for j in range(M):

                change = {'#' : '.', '.' : '#'}
                for c in change:
                    if arr[i][j] == c:
                        
                        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < N and 0 <= nj < M:
                                # 같은 것이 있다면 impossible 리턴
                                if arr[ni][nj] == c:
                                    return 'impossible'
                                
                                # '?'인 경우 '#' -> '.', '.' -> '#'으로 바꿈
                                elif arr[ni][nj] == '?':
                                    arr[ni][nj] = change[c]

        for row in arr:
            if '?' in row:  # '?'가 아직 있다면 다시 while문으로 돌아가.
                break
        else:  # '?'가 없다면 while문 빠져나가.
            break

    return 'possible'


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {Coloring()}')