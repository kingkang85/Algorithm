# D2
# 1959. 두 개의 숫자열       
t = int(input())

for i in range(1, t+1) :
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    lst = []   # result를 넣을 빈 리스트
    
    if n <= m :   
        while m >= n :   # A와 B의 길이가 같을 때까지만 실행
            result = 0   # result 초기화
            for j in range(n) :
                result += A[j]*B[j]   # 인덱스 번호가 같은 것끼리 곱해서 더함.
            lst.append(result)   # result 값을 lst에 추가
            B.pop(0)   # B의 첫번째 값을 제거
            m -= 1   # 위에서 하나 제거했으므로 m은 1만큼 줄어듦.
    else :
        while n >= m :
            result = 0
            for k in range(m) :
                result += A[k]*B[k]
            lst.append(result)
            A.pop(0)
            n -= 1
            
    print('#%d %d' %(i, max(lst)))   # lst 중 최댓값을 출력

####### 다른 풀이 #######
t = int(input())

for i in range(1, t+1) :
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if n > m : # B의 길이를 더 길게 !!
        n, m = m, n
        A, B = B, A 
        
    max_sum = 0
    for j in range(m-n+1) :
        temp = 0
        for k in range(n) :
            temp += A[k]*B[k+j]
        if temp > max_sum :
            max_sum = temp
    
    print('#%d %d' %(i, max_sum))
    
    
# 1961. 숫자 배열 회전
t = int(input())
for i in range(t) :
    n = int(input())
    arr = []
    result = []
    for j in range(n) :
        arr.append(list(map(int, input().split())))
        result.append([]) # 빈 행렬

    for k in range(n) :
        ans = ''
        for k2 in range(n-1, -1, -1) :
            ans += str(arr[k2][k])
        result[k].append(ans) # 90도 회전
        
    for l in range(n-1, -1, -1) :
        ans2 = ''
        for l2 in range(n-1, -1, -1):
            ans2 += str(arr[l][l2])
        result[n-l-1].append(ans2) # 180도 회전
    
    for h in range(n-1, -1, -1):
        ans3 = ''
        for h2 in range(n):
            ans3 += str(arr[h2][h])
        result[n-h-1].append(ans3) # 270도 회전
        
    print('#%d' %(i+1))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()

####### 다른 풀이 #######
def rotation(arr, n) :
    new_arr = [[0]*n for _ in range(n)] # nxn 빈 행렬
    for i in range(n) :
        for j in range(n) :
            new_arr[i][j] = arr[n-j-1][i]
    return new_arr

t = int(input())
for k in range(1, t+1) :
    n = int(input())
    arr = list(input().split() for _ in range(n))
    
    arr90 = rotation(arr, n)
    arr180 = rotation(arr90, n)
    arr270 = rotation(arr180, n)
    
    print('#%d' %k)
    for i,j,k in zip(arr90, arr180, arr270) :
        print(f"{''.join(i)} {''.join(j)} {''.join(k)}")
    
    
    
# 12712. 파리퇴치3
# t = int(input())
# for i in range(t) :
#     n, m = map(int, input().split())
#     arr = []
#     for j in range(n) :
#         arr.append(list(map(int, input().split())))
   

#     result = []
#     for k in range(n) :
#         for l in range(n) :
#             sum = 0
#             for k2 in (k-m+1, k+m) :
#                 if 0<=k2<n :
#                     sum += arr[k2][l]
            
#             for l2 in range(l-m+1, l+m) :
#                 if 0<=l2<n :
#                     sum += arr[k][l2]
#             sum -= arr[k][l]
#             result.append(sum)
        

    
#    # print('#%d %d'%(i+1, sum))