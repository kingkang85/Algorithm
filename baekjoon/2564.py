# 2564. 경비원
width, height = map(int, input().split())
stores = int(input())
st = []
for _ in range(stores):
    st.append(list(map(int, input().split())))  # k 방향, dist 거리

my_k, my_dist = map(int, input().split())  # my_k 동근이의 방향, my_dist 동근이의 거리

result = 0
for s in st:

    if my_k - s[0] == 0:
        if my_dist >= s[1]:
            result += my_dist - s[1]
        else:
            result += s[1] - my_dist

    elif my_k - s[0] == 1 or my_k - s[0] == -1:
        if s[0] == 1 or s[0] == 2:
            ans1 = my_dist + s[1] + height
            ans2 = 2 * width - my_dist - s[1] + height
            result += min(ans1, ans2)

    elif my_k - s[0] == 2 or my_k - s[0] == -2:
        my_dist + height - s[1]
        height + s[1] - my_dist
print(result)
