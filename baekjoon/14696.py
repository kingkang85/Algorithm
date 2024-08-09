# 14696. 딱지놀이
def WhoWin(A, B):
    # A와 B에 원소가 있어야 pop 가능
    # 마지막 원소인 최댓값이 pop !
    if A and B:
        childA = A.pop()
        childB = B.pop() 
    
        if childA > childB:
            return f'A'
    
        elif childA < childB:
            return f'B'

        # 최댓값이 같으면 다시 pop 반복
        else:
            return WhoWin(A, B)

    # 같은 딱지를 다 pop하고 원소가 남아있는 친구가 승 
    if A:
        return f'A'
    if B:
        return f'B'
    
    return f'D'  # 모든 경우를 만족하지 않으면 무승부
    
    
N = int(input())
for _ in range(N):
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    
    # 입력리스트의 인덱스 번호 1부터 정렬
    A = sorted(a_lst[1:])
    B = sorted(b_lst[1:])

    print(WhoWin(A, B))