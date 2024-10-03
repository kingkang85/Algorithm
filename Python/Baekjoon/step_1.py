# 1단계. 입출력과 사칙연산
# 2588. 곱셈
n1 = int(input())
n2 = input()
a = n1 * int(n2[-1])
b = n1 * int(n2[-2])
c = n1 * int(n2[-3])
d = a + b*10 + c*100
print(a)
print(b)
print(c)
print(d)


# 11382. 꼬마 정민
a, b, c = map(int, input().split())
print(a+b+c)


# 10171. 고양이
print("\    /\ \n )  ( ') \n(  /  ) \n \(__)|")


# 10172. 개
print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')
