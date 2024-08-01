x = int(input())
result = []
for i in range(x):
    y = int(input())
    li = list(map(int, input().split()))
    even_index_odd_value = 0
    odd_index_even_value = 0
    
    for i in range(y):
        if i % 2 == 0:
            if li[i] % 2 != 0:
                even_index_odd_value += 1
        else:
            if li[i] % 2 == 0:
                odd_index_even_value += 1
    
    
    if even_index_odd_value == odd_index_even_value:
        result.append(even_index_odd_value)
    else:
        result.append(-1)
for i in result:
    print(i)