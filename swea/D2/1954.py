# 1954. 달팽이 숫자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    row = col = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    k = 0  # 방향

    for num in range(1, N*N+1):
        arr[row][col] = num
        
        # 새로운 인덱스 번호
        newR = row + dr[k]
        newC = col + dc[k]
        
        # 벽을 만나거나 이미 값이 있다면 방향 다시 0으로
        if newR<0 or newR>=N or newC<0 or newC>=N or arr[newR][newC]:
            k = (k+1) % 4
        
        row += dr[k]
        col += dc[k]
        
    print(f'#{tc}')
    for data in arr:
        print(*data)

