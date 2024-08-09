# 10163. 색종이
N = int(input())

arr = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):
    r1, c1, r2, c2 = map(int, input().split())

    for r in range(r1, r1+r2):
        for c in range(c1, c1+c2):
            arr[r][c] = i


for j in range(1, N+1):
    cnt = 0
    for row in arr:
        for col in row:
            if col == j:
                cnt += 1
    print(cnt)