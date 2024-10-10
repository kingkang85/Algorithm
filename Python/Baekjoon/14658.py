# 14658. 하늘에서 별똥별이 빗발친다
import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]

minV = K
for i in range(K):
    for j in range(K):
        cnt = 0

        # 두 별을 걸치는 가장 왼쪽 상단 좌표
        starX, starY = min(stars[i][0], stars[j][0]), min(stars[j][1], stars[j][1])
        for x, y in stars:
            if starX <= x <= starX + L and starY <= y <= starY + L:
                continue
            cnt += 1
        
        minV = min(minV, cnt)

print(minV)
        