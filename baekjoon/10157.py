# 10157. 자리배정
C, R = map(int, input().split())  # 열 C, 행 R
K = int(input())
hall = [[0] * C for _ in range(R)]

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
k = 0  # 방향
i, j = R-1, 0  # 시작 인덱스

if K > C*R:  # 모든 자석이 배정된 경우
    print(0)

else:
    for num in range(1, K):  # K-1까지인 이유 => 그 다음 K의 인덱스를 얻기 위해
        hall[i][j] = num
        ni = i + d[k][0]
        nj = j + d[k][1]

        if ni<0 or ni>=R or nj<0 or nj>=C or hall[ni][nj]:
            k = (k+1) % 4  # 방향 바꿔줌

        i += d[k][0]
        j += d[k][1]
        # for문이 끝나면 i, j는 K의 인덱스가 됨

    print(j+1, R-i)  # 인덱스 번호와 좌석 번호를 비교하면
                     # 열 j+1, 행 R-i 과 같은 규칙을 알 수 있음