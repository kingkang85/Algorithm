# 1938. 아주 간단한 계산기
def Cal(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)

a, b = map(int, input().split())
Cal(a, b)