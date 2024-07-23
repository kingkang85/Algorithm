# 4406. 모음이 보이지 않는 사람
t = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(t):
    word = input()
    ans = ''
    for j in word :
        if j in vowels :
            continue
        else :
            ans += j
    print(f'#{i+1} {ans}')