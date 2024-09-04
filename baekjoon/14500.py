# 14500. 테트로미노
def is_valid_tetromino(squares):
    # 모든 칸이 연결되어 있는지 확인
    for i in range(3):
        diff = abs(squares[i+1][0] - squares[i][0]) + abs(squares[i+1][1] - squares[i][1])
        if diff != 1:
            return False
    
    # 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 확인
    x0, y0 = squares[0]
    x1, y1 = squares[1]
    x2, y2 = squares[2]
    x3, y3 = squares[3]
    
    # 가운데 칸을 기준으로 다른 세 칸이 붙어있는지 확인
    for i in range(4):
        center = squares[i]
        others = [s for j, s in enumerate(squares) if j != i]
        if all(abs(s[0] - center[0]) + abs(s[1] - center[1]) == 1 for s in others):
            return True
    
    return True  # 다른 모양들은 자동으로 처리됨

def get_comb(lev, start):
    global maxV
    if lev == 4:
        if is_valid_tetromino(squares):
            sumV = sum(arr[i][j] for i, j in squares)
            maxV = max(maxV, sumV)


        # sumV = 0
        # for i in range(3):
        #     if abs(squares[i+1][0] - squares[i][0] + squares[i+1][1] - squares[i][1]) != 1:
        #         break
        #     sumV += arr[squares[i][0]][squares[i][1]]

            # 뻐큐 모양은 따로 처리..
            # if squares[1][0] == squares[2][0] == squares[3][0] and squares[2][1] - squares[0][1] == 1:
            #     pass
            # if squares[0][0] == squares[1][0] == squares[2][0] and squares[3][1] - squares[1][1] == 1:
            #     pass
            # if squares[0][1] == squares[1][1] == squares[3][1] and squares[2][0] - squares[1][0] == 1:
            #     pass
            # if squares[0][1] == squares[2][1] == squares[3][1] and squares[2][0] - squares[1][0] == 1:
            #     pass
    
        # sumV += arr[squares[-1][0]][squares[-1][1]]

        # if maxV < sumV:
        #     maxV = sumV
        return
    
    # 2차원 배열을 1차원으로 쭈욱 펼침
    for idx in range(start + 1, N * M):
        i, j = idx // M, idx % M  # 행 인덱스는 열 개수로 나눈 몫
        squares.append([i, j])    # 열 인덱스는 열 개수로 나눈 나머지
        get_comb(lev + 1, start)
        squares.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

squares = []
maxV = 0
get_comb(0, -1)
print(maxV)

### 번뜩이는 아이디어!!!  인덱스를 뽑고 그게 테트로미노인지 확인 ?! ㄱㄱ
