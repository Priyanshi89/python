x = int(input())
if x <= 1000 and x>=1:
    for k in range(x):
        y = int(input())
        if y<=50 and y >=1:
            #li = []
            li = list(map(int, input().split()))
            li.sort()
            # for i in range(y):
            #     a = int(input())
            #     li.append(a)
            j = 0
            while j < len(li) - 1:
                if (li[j] - li[j+1] == 1) or (li[j] - li[j+1] == -1):
                    if li[j] > li[j+1]:
                        li.pop(j+1)
                    else :
                        li.pop(j)
                elif li[j] == li[j+1]:
                    li.pop(j)
                else:
                    j += 1
            if len(li) == 1:
                print("YES")
            else :
                print("NO")

