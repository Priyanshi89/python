x = int(input())
result = []
for i in range(x):
    li = list(map(int, input()))
    plus = True
    
    if li[0] + li[1] + li[2] == li[3] + li[4] + li[5]:
        plus = True
    else:
        plus = False
    if plus:
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)
