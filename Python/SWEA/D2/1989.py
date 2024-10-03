# 1989. 초심자의 회문 검사
T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1

    for i in range(N//2):
        if s[i] != s[N-1-i]:  # 맨 앞과 맨 뒤 글자가 다르면 ans = 0
            ans = 0
            break

    print(f'#{tc} {ans}')