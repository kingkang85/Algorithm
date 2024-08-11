# 2491. 수열
N = int(input())
seq = list(map(int, input().split()))

cnt = cnt2 = 1  # 자기 자신도 포함하므로
# Max = 0  # 0으로 초기화하면 원소가 하나있을 때 0 출력됨
Max = 1
for i in range(len(seq)-1):
    # 연속해서 커지는 것 찾기
    if seq[i] <= seq[i+1]:
        cnt += 1
        if Max < cnt:
            Max = cnt
    else:
        cnt = 1  # 더 작아지면 초기화


    # 연속해서 작아지는 것 찾기
    if seq[i] >= seq[i+1]:
        cnt2 += 1
        if Max < cnt2:
            Max = cnt2
    else:
        cnt2 = 1  # 더 작아지면 초기화

print(Max)
