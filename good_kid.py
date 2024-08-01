x = int(input())
result = []

for i in range(x):
    y = int(input())
    li = list(map(int, input().split()))
    initial_product = 1
    for i in li:
        initial_product*=i
    max_product = initial_product
    for i in range(len(li)):
        if li[i] == 0:
            new_product = initial_product * (li[i] + 1)
        else:
            new_product = (initial_product // li[i]) * (li[i] + 1)
        
        if new_product > max_product:
            max_product = new_product
        
    result.append(max_product)
for i in result:
    print(i)