# 10163. 색종이
N = int(input())

arr = [[0] * 18 for _ in range(18)]

for i in range(1, N+1):
    r1, c1, r2, c2 = map(int, input().split())
    arr[r1:r1+r2, c1:c1+c2]

for j in range(1, N+1):
    cnt = 0
    for row in arr:
        for col in row:
            if col == j:
                cnt += 1
    print(cnt)
