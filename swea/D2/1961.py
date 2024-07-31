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
# 1961. 숫자 배열 회전
def rotation(array, n):  # 90도 회전하는 함수
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = array[n-1-j][i] 
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr90 = rotation(arr, N)  # 90도 회전
    arr180 = rotation(arr90, N)  # 180도 회전
    arr270 = rotation(arr180, N)  # 270도 회전

    # print(arr90)
    # print(arr180)
    # print(arr270)
    # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]     
    
    # join은 문자열 메서드 !!!
    # TypeError: sequence item 0: expected str instance, int found
    # for i, j, k in zip(arr90, arr180, arr270):
    #     print(f"{''.join(i)} {''.join(j)} {''.join(k)}")

    print(f'#{tc}')
    for i, j, k in zip(arr90, arr180, arr270):
        print(f"{''.join(i)} {''.join(j)} {''.join(k)}")