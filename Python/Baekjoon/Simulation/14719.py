# 14719. 빗물
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
arr = [[0] * W for _ in range(H)]

# 이차원 배열에 블록 1로 채우기
for j in range(W):
    for i in range(H-1, H-blocks[j]-1, -1):
        arr[i][j] = 1

maxH = max(blocks)  # 블록의 최대 높이
total = 0  # 빗물의 총량
for i in range(H-maxH, H):
    for j in range(W):
        cnt = 0

        # 1로 시작하고 1로 끝나는 부분 0 개수 세기
        if arr[i][j] == 1:
            next = j + 1
            while next < W and arr[i][next] == 0:
                cnt += 1
                next += 1

            # 0으로 끝나면 막아주는 블록이 없으므로 cnt 초기화
            if next == W:
                cnt = 0
        total += cnt

print(total)