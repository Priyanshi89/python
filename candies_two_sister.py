# x = int(input())
# result=[]
# for i in range(x):
#     count =  0
#     y = int(input())
#     for a in range(y-1, y//2, -1):
#         b = y-a
#         count = count +1
#     result.append(count)
# for i in result:
#     print(i)

x = int(input())
result = []

for _ in range(x):
    y = int(input())
    count = (y - 1) // 2
    result.append(count)

for i in result:
    print(i)
