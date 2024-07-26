# 1966. 숫자를 정렬하자
t = int(input())

for i in range(t):
    n = int(input())
    
    # n개의 숫자를 입력받아 리스트로 변환
    num_lst = list(map(int, input().split()))
    
    # 오름차순 정렬
    num_lst.sort()
    
    print(f'#{i+1}', end=' ')  
    for num in num_lst:
        print(num, end=' ')  # 리스트 순회하며 정렬된 숫자 출력   
    
    print()  # 반복마다 개행을 위한 프린트문