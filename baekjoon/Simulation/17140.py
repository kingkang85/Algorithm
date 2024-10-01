# 17140. 이차원 배열과 연산
import sys
input = sys.stdin.readline

def Cal():
    max_len = 0  # 가장 긴 행의 길이
    for i in range(len(arr)):
        # 각 숫자의 등장 횟수 카운트
        count = [0] * 101
        for num in arr[i]:
            if num != 0:
                count[num] += 1

        lst = []  # (숫자, 등장 횟수)를 저장할 리스트
        for num in range(1, 101):
            if count[num] > 0:
                lst.append((num, count[num]))

        # 등장 횟수를 기준으로 정렬
        lst.sort(key = lambda x: x[1])

        # 정렬된 쌍을 펼쳐 새 행 만들기
        new_row = []
        for num, cnt in lst:
            new_row.extend([num, cnt])

        arr[i] = new_row[:100]  # 100개까지 자르기
        max_len = max(max_len, len(arr[i]))

    # max_len에 맞춰 나머지 0으로 채우기
    for row in arr:
        row += [0] * (max_len - len(row))
    
    return len(arr), max_len  # 새로운 행의 수와 열의 수 반환

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
nrow, ncol = 3, 3
while time <= 100:
    if r <= nrow and c <= ncol and arr[r-1][c-1] == k:
        print(time)
        break

    time += 1

    # R 연산
    if nrow >= ncol:
        nrow, ncol = Cal()
    
    # C 연산
    else:
        arr = list(map(list, zip(*arr)))  # 전치 행렬
        ncol, nrow = Cal()  # (주의) 행과 열 개수 뒤바뀜
        arr = list(map(list, zip(*arr)))

else:
    print(-1)