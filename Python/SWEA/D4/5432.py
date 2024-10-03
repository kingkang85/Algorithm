# 5432. 쇠막대기 자르기
T = int(input())
for tc in range(1, T+1):
    sticks = input()

    cnt = 0
    total = 0
    for i in range(len(sticks)):
        if sticks[i] == '(':
           cnt += 1

        elif sticks[i] == ')':
            cnt -= 1
            if sticks[i-1] == '(':
                total += cnt

            else:  # 맨 끝 막대기 추가
                total += 1

    print(f'#{tc} {total}')