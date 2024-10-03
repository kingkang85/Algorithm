# 14555. 공과 잡초
T = int(input())
for tc in range(1, T+1):
    S = input()

    cnt = 0  # 공 개수
    for i in range(len(S)-1):
        if S[i] == '(' and S[i+1] == '|':
            cnt += 1
        if S[i] == '|' and S[i+1] == ')':
            cnt += 1
        if S[i] == '(' and S[i+1] == ')':
            cnt += 1
    
    print(f'#{tc} {cnt}')