# 2628. 종이 자르기
w, h = map(int, input().split())
cut_lines = int(input())

# 가로 세로의 잘린 포인트를 담기 위한 리스트
# 앞뒤 비교하며 길이를 비교하기 위해 첫과 끝도 추가했음
row = [0] + [h]
col = [0] + [w]

for _ in range(cut_lines):
    standard, cut = map(int, input().split())

    if standard == 0:  # 가로 cutting 포인트
        row.append(cut)
    else:  # 세로 cutting 포인트
        col.append(cut)

row.sort()
col.sort()

# print(row, col)  # [0, 2, 3, 8] [0, 4, 10]

Max = 0
for i in range(len(row)-1):
    for j in range(len(col)-1):
        # 뒤에서 앞 빼면서 넓이 구하기
        area = (row[i+1] - row[i]) * (col[j+1] - col[j])

        # 최댓값 찾기
        if Max < area:
            Max = area

print(Max)

