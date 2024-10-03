# 2578. 빙고
def Bingo(check):
    bingo_cnt = 0
    for i in range(5):
        # 가로 확인
        if sum(check[i]) == 0:
            bingo_cnt += 1
        
        # 세로 확인
        if sum(row[i] for row in check) == 0:
            bingo_cnt += 1

    # 대각선 확인
    if sum(check[i][i] for i in range(5)) == 0:
        bingo_cnt += 1

    if sum(check[i][4-i] for i in range(5)) == 0:
        bingo_cnt += 1

    return bingo_cnt     
             

my_bingo = [list(map(int, input().split())) for _ in range(5)]
call_numbers = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
for row in call_numbers:
    for num in row:
        cnt += 1

        # 내 빙고판에서 부른 숫자 찾기
        for i in range(5):
            for j in range(5):
                if my_bingo[i][j] == num:
                    my_bingo[i][j] = 0  # 부른 숫자에 0 재할당
                    break  # num을 찾았으므로 for j를 빠져나감

            else:  # num을 찾지 못한 경우 다음 행으로 넘어감
                continue

            break  # num을 찾았으므로 for i를 빠져나감
        
        # 세 줄 빙고 확인
        if Bingo(my_bingo) >= 3:
            print(cnt)
            break  # 세 줄 빙고이면 for num 빠져나감
    
    else:
        continue

    break
