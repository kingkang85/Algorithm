#1283. 단축키 지정
import sys
input = sys.stdin.readline

N = int(input())
arr = [input().split() for _ in range(N)]
new_arr = [[[] for _ in range(len(arr[i]))] for i in range(N)]
for i in range(N):
    for j in range(len(arr[i])):
        for _ in range(len(arr[i][j])):
            new_arr[i][j].append('')

short = set()
for i in range(N):
    for j in range(len(arr[i])):
        if arr[i][j][0].upper() not in short:
            short.add(arr[i][j][0].upper())
            new_arr[i][j][0] = '[' + arr[i][j][0] + ']'
            break
        
    else:
        found = False
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                if arr[i][j][k].upper() not in short:
                    found = True
                    short.add(arr[i][j][k].upper())
                    new_arr[i][j][k] = '[' + arr[i][j][k] + ']'
                    break

            if found:
                break


for i in range(N):
    for j in range(len(new_arr[i])):
        for k in range(len(new_arr[i][j])):
            if new_arr[i][j][k] == '':
                new_arr[i][j][k] = arr[i][j][k]

for i in range(N):
    for j in range(len(new_arr[i])):
        for k in range(len(new_arr[i][j])):
            print(new_arr[i][j][k], end='')
        print(end=' ')
    print()