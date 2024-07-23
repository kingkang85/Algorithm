# 2050. 알파벳을 숫자로 변환
alpha = input()
for i in alpha:
    print(ord(i)-64, end=' ')