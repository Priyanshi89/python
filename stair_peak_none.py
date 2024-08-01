x = int(input())
result = []
for i in range(x):
    li = list(map(int, input().split()))
    instance = False
    instance1 = False
    if li[0] < li[1]:
        if li[1] < li[2]:
            instance = True
        elif li[1] > li[2]:
            instance1 = True
    if instance:
        result.append("STAIR")
    elif instance1:
        result.append("PEAK")
    else:
        result.append("NONE")

for i in result:
    print(i)
