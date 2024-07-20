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