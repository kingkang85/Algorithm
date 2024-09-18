# 10814. 나이순 정렬
import sys
input = sys.stdin.readline

N = int(input())
ppl = []
for i in range(N):
    age, name = input().split()
    ppl.append((int(age), i, name))

ppl.sort()
for data in ppl:
    print(data[0], data[2])