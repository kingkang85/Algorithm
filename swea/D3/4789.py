# 4789. 성공적인 공연 기획
T = int(input())
for tc in range(1, T+1):
    info = input()
    clap = int(info[0])
    need = len(info) - 1

    for j in range(1, len(info)):
        if j == clap:
            clap += int(info[j])

        else:
            if info[j] == '0':
                need = need - (j - clap)
                clap += need + int(info[j])
            # else:
            #     need = need - (j - clap)
            #     clap += need + int(info[j])

    print(f'#{tc} {need}')
