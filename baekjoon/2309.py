# 2309. 일곱 난쟁이
# 부분집합 이용
heights = []
for _ in range(9):
    h = int(input())
    heights.append(h)  # 아홉 난쟁이들의 키를 리스트에 추가

N = len(heights)
for i in range(1<<N):  # 부분집합의 총 개수
    subset = []
    for j in range(N):
        if i & (1<<j):  # 1이면 부분집합에 추가
            subset.append(heights[j])

    # 키의 합이 100인 리얼 일곱 난쟁이들
    if len(subset) == 7 and sum(subset) == 100:
        subset.sort()
        for k in subset:
            print(k)
        break