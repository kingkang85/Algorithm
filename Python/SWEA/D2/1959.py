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