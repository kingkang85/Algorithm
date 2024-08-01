# 13300. 방 배정
N, K = map(int, input().split())
arr = [[0] * 2 for i in range(6)]

for _ in range(N):
    s, y = map(int, input().split())
    arr[y-1][s] += 1
    

for i in range(len(lst)):

    if lst.count(lst[i]) <= 2:
        cnt += 1
        print(cnt)
    else:
        cnt += int(lst.count(lst[i])/2)

print(cnt)




