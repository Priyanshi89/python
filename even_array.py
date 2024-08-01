n = int(input())
zero = 0
one = -1
count_zero = []

for i in range(n):
    y = int(input())
    li = list(map(int, input().split()))
    if len(li) == 1:
        if li[0] % 2 == 0:
            count_zero.append(zero)
        else:
            count_zero.append(one)
    else:
        for i in range(len(li)):
            count_one = []
            if i%2 == li[i]%2:
                count_one.append(zero)
        if one not in count_one:
            count_zero.append(zero)
            if i%2 != li[i]%2:
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp
                
print(count_zero)
print(len(count_zero))
for i in range(len(count_zero)):
    print(count_zero[i])