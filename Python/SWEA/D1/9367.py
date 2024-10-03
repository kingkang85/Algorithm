# 9367. 점점 커지는 당근의 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    Max = 1
    cnt = 1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            cnt += 1
        else:
            if Max < cnt:
                Max = cnt
            cnt = 1
        
        if Max < cnt:
            Max = cnt

    print(f'#{tc} {Max}')