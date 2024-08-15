# 4789. 성공적인 공연 기획
T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input()))
    clap = info[0]
    need = 0

    for i in range(1, len(info)):
        if info[i] == 0:
            continue

        if i <= clap:
            clap += info[i]

        else:
            need += i - clap
            clap += i - clap + info[i]

    print(f'#{tc} {need}')