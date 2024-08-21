# 2805. 농작물 수확하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    get = 0
    for i in range(N):
        if i <= N//2:
            get += sum(farm[i][N//2-i : N//2+i+1])

        else:
            get += sum(farm[i][N//2-(N-1-i) : N//2+(N-i)])
        
    print(f'#{tc} {get}')