x = int(input())
result = []

for _ in range(x):
    y = int(input())  
    li = list(map(int, input().split()))

    
    initial_product = 1
    zero_count = li.count(0)
    

    if zero_count > 0:
        
        initial_product = 1
        for digit in range(len(li)-1):
            if li[digit] == 0:
                li[digit] = li[digit] +1
                for i in li:
                    initial_product*=i
                

        max_product = initial_product
        
    else:
        
        initial_product = 1
        for digit in li:
            initial_product *= digit

        max_product = initial_product
        for i in range(len(li)):
            new_product = (initial_product // li[i]) * (li[i] + 1)
            if new_product > max_product:
                max_product = new_product

    result.append(max_product)

for res in result:
    print(res)
