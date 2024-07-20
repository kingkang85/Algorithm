# 3단계. 반복문
# 2739. 구구단
n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n*i)


# 10950. A+B - 3
T = int(input())
for i in range(1, T+1) :
    A, B = map(int, input().split())
    print(A+B)


# 8393. 합
n = int(input())
sum = 0
for i in range(1, n+1) :
    sum += i
print(sum)


# 25304. 영수증
X = int(input())
N = int(input())
sum = 0
for i in range(1, N+1) :
    a, b = map(int, input().split())
    sum += a*b
if sum == X :
    print('Yes')
else :
    print('No')


# 25314. 코딩은 체육 과목입니다
N = int(input())
while 1 :
    print('long '*(N//4) + 'int')
    break


# 15552. 빠른 A+B
# https://yeomss.tistory.com/120
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
import sys
T = int(sys.stdin.readline())
for i in range(T) :
    n, m = map(int, sys.stdin.readline().split())
    print(n+m)
    

# 11021. A+B - 7
T = int(input())
for i in range(T) :
    a, b = map(int, input().split())
    print('Case #%d: %d' % (i+1, a+b))
    
T = int(input())
for i in range(T) :
    a, b = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(i+1, a, b, a+b))

    
# 2438. 별 찍기 - 1
n = int(input())
for i in range(1, n+1) :
    print('*'*i)


# 2439. 별 찍기 - 2
n = int(input())
for i in range(1, n+1) :
    print(' '*(n-i)+'*'*i)
    

# 10952. A+B - 5 
while True :
    a, b = map(int, input().split())
    if (a==0) & (b==0) :
        break
    print(a+b)
    

# 10951. A+B -4
while True :
    try :
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except :
        break