x = int(input())
result = []
for i in range(x):
    li = list(map(int, input().split()))
    plus = True
    
    if li[0] + li[1] == li[2]:
        plus = True
    else:
        plus = False
    if plus:
        result.append("+")
    else:
        result.append("-")
for i in result:
    print(i)
    
