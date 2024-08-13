# 4789. 성공적인 공연 기획
T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input()))
    clap = info[0]
    need = 0

    for j in range(1, len(info)):
        if info[j] == 0:
            continue

        else:
            if j == clap:
                clap += info[j]

            else:
                need += (j - clap)
                clap += need + info[j]

    print(f'#{tc} {need}')
