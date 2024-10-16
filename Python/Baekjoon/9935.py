# 9935. 문자열 폭발
import sys
input = sys.stdin.readline

string = input().strip()
boom = input().strip()
n = len(boom)  # 폭탄 문자열의 길이
result = []  # 결과를 담을 리스트

# 문자를 result에 하나씩 추가
for s in string:
    result.append(s)
    # 폭탄 문자열의 마지막 글자와 같으면 폭탄 문자열인지 확인
    if s == boom[-1] and ''.join(result[-n:]) == boom:
        # 맞다면 폭탄 문자열의 길이만큼 pop
        for _ in range(n):
            result.pop()

if result:
    print(''.join(result))
else:
    print('FRULA')