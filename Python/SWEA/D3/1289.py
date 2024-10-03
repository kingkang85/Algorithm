# 1289. 원재의 메모리 복구하기
T = int(input())
for tc in range(1, T+1):
    org_memory = list(input())
    N = len(org_memory)

    cnt = 0
    while 1:
        try:
            start = org_memory.index('1')
        except:
            break

        for i in range(start, N):
            if org_memory[i] == '1':
                org_memory[i] = '0'
            else:
                org_memory[i] = '1'
        
        cnt += 1

    print(f'#{tc} {cnt}')

    # cnt = 0
    # for i in range(N):
    #     if org_memory[i] == '1':
    #         start = org_memory[i]
    #         cnt += 1

    #         for j in range(int(start), N):
    #             if org_memory[j] == '1':
    #                 org_memory[j] = '0'

    #             else:
    #                 org_memory[j] = '1'
        
    # print(f'#{tc} {cnt}')
