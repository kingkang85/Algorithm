# 2056. 연월일 달력
t = int(input())
for i in range(t):
    date = input()
    yyyy = date[:4]
    mm = date[4:6]
    dd = date[6:]
    if int(mm) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(dd) <= 31:
        print(f'#{i+1} {yyyy}/{mm}/{dd}')
    elif int(mm) in [4, 6, 9, 11] and 1 <= int(dd) <= 30:
        print(f'#{i+1} {yyyy}/{mm}/{dd}')
    elif int(mm) == 2 and 1 <= int(dd) <= 28:
        print(f'#{i+1} {yyyy}/{mm}/{dd}')
    else:
        print(f'#{i+1} -1')