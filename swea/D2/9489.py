# 9489. 고대 유적
def MaxLength():
    MaxV = 0
    # 가로 확인
    for i in range(N):
        cnt = 0
        for j in range(M):
            if image[i][j] == 1:  # 1이면 cnt 1 증가
                cnt += 1

            else:  # 0이면 최댓값 비교 후 cnt 초기화
                if MaxV < cnt:
                    MaxV = cnt
                cnt = 0

        if MaxV < cnt:  # 마지막 열이 1인 경우 대비
            MaxV = cnt
        
    # 세로 확인   
    for j in range(M):
        cnt = 0
        for i in range(N):
            if image[i][j] == 1:
                cnt += 1

            else:
                if MaxV < cnt:
                    MaxV = cnt
                cnt = 0

        if MaxV < cnt:  # 마지막 행이 1인 경우 대비
            MaxV = cnt
    
    return MaxV


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {MaxLength()}')