# 2564. 경비원
width, height = map(int, input().split())
stores = int(input())
st = []
for _ in range(stores+1):
    st.append(list(map(int, input().split())))  # k 방향, dist 거리

result = []
for s in st:
    if s[0] == 3:
        result.append(s[1])

    elif s[0] == 2:
        result.append(height + s[1])

    elif s[0] == 4:
        result.append(2*height+width-s[1])

    else:
        result.append(2*height+2*width-s[1])

sumV = 0
for dist in result[:stores]:
    minV = min(abs(result[stores] - dist), abs(2*height+2*width + result[stores] - dist))
    sumV += minV
print(sumV)