# 10157. 자리배정
C, R = map(int, input().split())
K = int(input())
hall = [[0] * C for _ in range(R)]

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
k = 0
i, j = R-1, 0

if K > C*R:
    print(0)

else:
    for num in range(1, K+1):
        hall[i][j] = num
        ni = i + d[k][0]
        nj = j + d[k][1]

        if ni<0 or ni>=R or nj<0 or nj>=C or hall[ni][nj]:
            k = (k+1) % 4

        i += d[k][0]
        j += d[k][1]

    print(j+1, R-i)


