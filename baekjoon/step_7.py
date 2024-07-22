# 7단계. 2차원 배열
# 2738. 행렬 덧셈
n, m = map(int, input().split())
arr1 = [input().split() for _ in range(n)]
arr2 = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(m):
        sum = int(arr1[i][j]) + int(arr2[i][j])
        print(sum, end=' ')
    print()