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