# 1912. 연속합
N = int(input())
seq = list(map(int, input().split()))

# 누적 값보다 현재 값이 더 크면 현재 값부터 다시 시작한다고 생각하자!
for i in range(1, N):
    seq[i] = max(seq[i], seq[i] + seq[i-1])

print(max(seq))