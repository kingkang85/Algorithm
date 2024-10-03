# 14891. 톱니바퀴
import sys
input = sys.stdin.readline

arr = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())

    start, direct = n-1, d
    rotate = [(start, direct)]
    
    # 왼쪽 톱니바퀴 담기
    for i in range(start, 0, -1):
        if arr[i][6] != arr[i-1][2]:
            direct *= -1
            rotate.append((i-1, direct))
        else:
            break
    
    # 오른쪽 톱니바퀴 담기
    direct = d  # 방향 초기화
    for i in range(start, 3):
        if arr[i][2] != arr[i+1][6]:
            direct *= -1
            rotate.append((i+1, direct))
        else:
            break
    
    # 톱니바퀴 회전 시키기
    while rotate:
        cog, dd = rotate.pop()
        # 시계 방향
        if dd == 1:
            arr[cog] = [arr[cog][-1]] + arr[cog][:-1]
        # 반시계 방향
        else:
            arr[cog] = arr[cog][1:] + [arr[cog][0]]

# 점수 계산
score = 0
for i in range(4):
    score += arr[i][0] * (1<<i)

print(score)