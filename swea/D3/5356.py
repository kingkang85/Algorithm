# 5356. 의석이의 세로로 말해요
# T = int(input())
# for tc in range(1, T+1):
#     words = [input() for _ in range(5)]
#     result = [[0] * 15 for _ in range(5)]

#     for i in range(5):
#         for j in range(len(words[i])):
#             result[i][j] = words[i][j]

#     ans = ''
#     for j in range(15):
#         for i in range(5):
#             if result[i][j] != 0:
#                 ans += result[i][j]

#     print(f'#{tc} {ans}')


##### 다른 풀이 #####
T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]

    ans = ''
    for i in range(15):
        for row in words:
            if i < len(row):
                ans += row[i]
    
    print(f'#{tc} {ans}')