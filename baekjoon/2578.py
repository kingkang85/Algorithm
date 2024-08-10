# 2578. 빙고
def Bingo(check):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if check[i][j] != 0:
                break
        else:
            cnt += 1
    for i in range(5):
        for j in range(5):
            if check[i][j] != 0:
                break
        else:
            cnt += 1
    
    for i in range(5):
        if check[i][i] != 0:
            break
        else:
            cnt += 1

    for i in range(5):
        if check[i][4-i] != 0:
            break
        else:
            cnt += 1

    return cnt
    

                
             


my_bingo = [list(map(int, input().split())) for _ in range(5)]
correct_bingo = [list(map(int, input().split())) for _ in range(5)]


cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        num = correct_bingo[i][j]

        for i in range(5):
            for j in range(5):
                if my_bingo[i][j] == num:
                    my_bingo[i][j] = 0

        if Bingo(my_bingo) == 3:
            print(cnt)
            break

    break



