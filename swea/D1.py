# D1
# 1936. 1대1 가위바위보
T = list(map(int, input().split()))

if T[0]==1 :
    if T[1]==2 :
        print('B')
    else :
        print('A')
elif T[0]==2 :
    if T[1]==1 :
        print('A')
    else :
        print('B')
else :
    if T[1]==1 :
        print('B')
    else :
        print('A')
    

# 2058. 자릿수 더하기
N = int(input())

a = N//1000
b = (N%1000)//100
c = (N%100)//10
d = N%10

print(a+b+c+d)

###### 다른 풀이 ######
N = int(input())

sum = 0
for i in str(N) :
    sum += int(i)
print(sum)


# 2063. 중간값 찾기
N = int(input())
score = sorted(map(int, input().split()))
median = score[N//2]
print(median)