# 2628. 종이 자르기
r, c = map(int, input().split())
arr = [[0] * c for _ in range(r)]
cut_lines = int(input())

for _ in range(cut_lines):
    standard, cut = map(int, input().split())

    # 가로로 자를 때
    if standard == 0:
        arr = arr[:cut][:]
        print(arr)

    # 세로로 자를 때
    else:
        arr = arr[:][:cut]

        print(arr)



