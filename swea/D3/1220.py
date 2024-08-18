# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
def Magnetic():
    cnt = 0
    for j in range(n):
        for i in range(n):
            # 열 탐색          
            if table[i][j] == 1:
                for i2 in range(i+1, n):   # 1 이후로
                    if table[i2][j] == 1:  # 다시 1을 만나면 break
                        break

                    elif table[i2][j] == 2:  # 2를 만나면 cnt 1 증가 후 break
                        cnt += 1
                        break
    
    return cnt
            

for tc in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {Magnetic()}')