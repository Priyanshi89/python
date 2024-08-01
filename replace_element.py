n = int(input())
result = []
for i in range(n):
    li = list(map(int, input().split()))
    li1 = list(map(int, input().split()))
    if all(x<=li[1] for x in li1):
        result.append("YES")
    else:
        li1.sort()
        if li1[0] + li1[1] <= li[1]:
            result.append("YES")
        else:
            result.append("NO")
for i in result:
    print(i)