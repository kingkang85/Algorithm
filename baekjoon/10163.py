# 10163. 색종이
N = int(input())


idx_lst = []
for i in range(1, N+1):
    r1, c1, r2, c2 = map(int, input().split())
    idx_lst.append([r1, r1+r2, c1, c1+c2])
Max = max(idx_lst)
arr = [[0]*]

for j in range(1, N+1):
    cnt = 0
    for row in arr:
        for col in row:
            if col == j:
                cnt += 1
    print(cnt)
