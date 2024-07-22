# 문자열
# 27866. 문자와 문자열
s = input()
i = int(input())
print(s[i-1]) # 문자열 인덱싱 가능

# 11654. 아스키 코드
letter = input()
print(ord(letter))

# 11720. 숫자의 합
n = int(input())
nums = list(map(int, input()))
print(sum(nums))

# 10809. 알파벳 찾기
s = input()
    
for i in range(ord('a'), ord('z')+1) :
    print(s.find(chr(i)), end=' ')

# 2908. 상수
a, b = input().split()
ans1 = int(a[::-1])
ans2 = int(b[::-1])

if ans1 > ans2 :
    print(ans1)
else :
    print(ans2)

# 5622. 다이얼
calling_num = input()
dial = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in calling_num:
    for j in dial:
        if i in j:
            time += dial.index(j)
print(time)

# 11718. 그대로 출력하기
while True:
    try:
        print(input())
    except EOFError:
        break

import sys
lines = sys.stdin.readlines()
for words in lines:
    print(words.rstrip())