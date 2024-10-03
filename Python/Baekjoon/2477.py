# 2477. 참외밭
K = int(input())  # 1m^2의 넓이에서 자라는 참외의 개수
melon = []
for _ in range(6):
    d, l = map(int, input().split())
    melon.append((d, l))

for i in range(6):
    if (melon[i-1][0], melon[i][0]) == (1, 3) or \
       (melon[i-1][0], melon[i][0]) == (4, 1) or \
       (melon[i-1][0], melon[i][0]) == (2, 4) or \
       (melon[i-1][0], melon[i][0]) == (3, 2):
        
        minus_area = melon[i-1][1] * melon[i][1]
        j1 = melon[i-1][0]
        j2 = melon[i][0]
        break

total_area = 1
for k in range(6):
    if melon[k][0] not in [j1, j2]:
        total_area *= melon[k][1]

result = (total_area - minus_area) * K
print(result)