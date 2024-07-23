# 2063. 중간값 찾기
N = int(input())
score = sorted(map(int, input().split()))
median = score[N//2]
print(median)