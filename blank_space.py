x = int(input())

for i in range(x):
    y = int(input())
    li = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(len(li)):
        if li[i] == 0 :
            count = count+1
        
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)

