# 2058. 자릿수 더하기
N = int(input())

a = N//1000
b = (N%1000)//100
c = (N%100)//10
d = N%10

print(a+b+c+d)

###### 다른 풀이 ######
N = input()

sum = 0
for i in N:
    sum += int(i)
print(sum)