# 2단계. 조건문
# 1330. 두 수 비교하기
a, b = map(int, input().split())
if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')
    
# 9498. 시험 성적
n = int(input())
if 90 <= n <= 100 :
    print('A')
elif 80 <= n <= 89 :
    print('B')
elif 70 <= n <= 79 :
    print('C')
elif 60 <= n <= 69 :
    print('D')
else :
    print('F')
    
# 2753. 윤년
year = int(input())
if (year%4 == 0) & (year%100 != 0) | (year%400 == 0) :
    print(1)
else :
    print(0)
    
# 14681. 사분면 고르기
x = int(input())
y = int(input())
if (x>0) & (y>0) :
    print(1)
elif (x<0) & (y>0) :
    print(2)
elif (x<0) & (y<0) :
    print(3)
else :
    print(4)

# 2884. 알람 시계
H, M = map(int, input().split())
if M < 45 :
    if H == 0 :
        H = 23
    else :
        H -= 1
    M = 60 - (45-M)
else :
    M -= 45
print(H, M)

# 2525. 오븐 시계
A, B = map(int, input().split())
C = int(input())
if (B+C) >= 60 :
    A += (B+C)//60
    B = (B+C)%60
    if A >= 24 :
        A %= 24
else :
    B += C
print(A, B)
    
# 2480. 주사위 세 개
a, b, c = map(int, input().split())
if a == b == c :
    price = 10000 + a*1000
elif (a==b) | (a==c) :
    price = 1000 + a*100
elif (b==c) :
    price = 1000 + b*100
else :
    n = max(a, b, c)
    price = n*100
print(price)