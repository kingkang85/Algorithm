# 4단계. 1차원 배열
# 10807. 개수 세기
n = int(input())
nums = list(map(int, input().split()))
v = int(input())
sum = 0
for i in nums :
    if i == v :
        sum += 1
print(sum)


# 10871. X보다 작은 수
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in a :
    if i < x :
        print(i, end=' ')


# 10818. 최소, 최대
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))


# 2562. 최댓값
lst = []
for _ in range(9) :
    n = int(input())
    lst.append(n)
ans = max(lst)
print(ans, lst.index(ans)+1)


# 10810. 공 넣기
n, m = map(int, input().split())
lst = [0]*n

for i in range(m) :
    a, b, c = map(int, input().split())
    for l in range(a-1, b) :
        lst[l] = c

for i in lst :
    print(i, end=' ')


# 10813. 공 바꾸기
n, m = map(int, input().split())
lst = []
for i in range(1, n+1) :
    lst.append(i)

for i2 in range(m) :
    a, b = map(int, input().split())
    lst[a-1], lst[b-1] = lst[b-1], lst[a-1]

for j in lst :
    print(j, end=' ')
    

# 5597. 과제 안 내신 분..?
lst = []
for i in range(1, 29) :
    n = int(input())
    lst.append(n)
    
for j in range(1, 31) :
    if j not in lst :
        print(j)

###### 다른 풀이 ######
Total_Student = [i for i in range(1, 31)]

for _ in range(28) :
    Pass_Student = int(input())
    Total_Student.remove(Pass_Student)

print(min(Total_Student))
print(max(Total_Student))            
        

# 3052. 나머지
result = []
for i in range(10) :
    n = int(input())
    ans = n%42
    if ans not in result :
        result.append(ans) 
print(len(result))
        
###### 다른 풀이 ######
# 집합은 중복이 안 된다는 특징 이용
result = set()
for _ in range(10) :
    n = int(input())
    result.add(n%42)
print(len(result))
    

# 10811. 바구니 뒤집기
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
    
for _ in range(m) :
    a, b = map(int, input().split())
    temp = lst[a-1:b]
    temp.reverse()
    lst[a-1:b] = temp

for j in lst :
    print(j, end=' ')
        

# 1546. 평균
n = int(input())
scores = list(map(int, input().split()))
Max = max(scores)

for i in range(n) :
    scores[i] = scores[i]/Max*100
    
ans = sum(scores) / len(scores)
print(ans)