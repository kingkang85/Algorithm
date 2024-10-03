# 11722. 가장 긴 감소하는 부분 수열
N = int(input())
seq = list(map(int, input().split()))
lds = [1] * N  # 각 위치에서의 길이 저장

for i in range(1, N):
    for j in range(i):
        # 감소하고 최장인지 확인
        if seq[j] > seq[i] and lds[i] < lds[j] + 1:
            lds[i] = lds[j] + 1

print(max(lds))