# 4613. 러시아 국기 같은 깃발
def Cal(wb, br):
    sumV = 0
    for i in range(0, wb):
        sumV += counts[i][1] + counts[i][2]
    for i in range(wb, br+1):
        sumV += counts[i][0] + counts[i][2]
    for i in range(br+1, N):
        sumV += counts[i][0] + counts[i][1]

    return sumV

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    counts = [[0, 0, 0] for _ in range(N)]  # 각 줄의 색깔 개수
    for i in range(N):
        counts[i][0] = arr[i].count('W')
        counts[i][1] = arr[i].count('B')
        counts[i][2] = arr[i].count('R')

    # 경계 구하기
    minV = N*M
    for wb in range(1, N-1):  # 적어도 파랑 한 줄, 빨강 한 줄 있어야함
        for br in range(wb, N-1):  # 적어도 빨강 한 줄 있어야함
           val = Cal(wb, br)  # 파랑의 범위라고 생각하면 편함
           if minV > val:
               minV = val

    print(f'#{tc} {minV}')