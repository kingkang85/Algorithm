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


# 2566. 최댓값
arr = [list(map(int, input().split())) for _ in range(9)]
Max, row, col = arr[0][0], 0, 0  # Max의 초기값을 배열의 1행 1열 값으로 설정
for i in range(9):
    for j in range(9):
       if Max <= arr[i][j]:  # 등호 주의
           Max = arr[i][j]
           row, col = i+1, j+1  # i, j는 인덱스이므로 1씩 증가

print(Max)
print(row, col)
