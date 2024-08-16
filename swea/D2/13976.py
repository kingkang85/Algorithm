# 13976. 기지국
def check():
    
    for i in range(n):
        for j in range(n):
            di = [1, 0, -1, 0]
            dj = [0, 1, 0, -1]

            if arr[i][j] == 'X':
                continue

            elif arr[i][j] == 'A':
                ni = i + di
                nj = j + dj

            elif arr[i][j] == 'B':
                ni = i + di * 2
                nj = j + dj * 2
            
            elif arr[i][j] == 'C':
                ni = i + di * 3
                nj = j + dj * 3

            if 0 <= ni < n and 0 <= nj < n:
                pass


                

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    total = 0
    for i in range(n):
        total += arr[i].count('H')
    
    print(total)


    