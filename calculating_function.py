# def calculate(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + (-1)**(i) * i
#     return sum
def calculate(n):
    if n % 2 == 0:
        return n // 2
    else:
        return -(n + 1) // 2


x = int(input())
ans = calculate(x)
print(ans)

