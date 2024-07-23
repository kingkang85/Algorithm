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