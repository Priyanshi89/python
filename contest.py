# n = int(input())
# result = []
# for i in range(n):
#     y = int(input())
#     list = list(map(int, input().split()))
#     for _ in range(40):
#         op = []
#         if all(i==0 for i in list):
#             result.append(0)
#         else:
#             x = max(list)
#             op.append(x)
#             list = [abs[i-x] for i in list]
#             if all(x==0 for x in list):
#                 result.append(f"{len(op)}")
#                 result.append(" ".join(map(str, op)))
#             else:
#                 result.append(-1)
# for i in result:
#     print(i)
# n = int(input())
# result = []
# for i in range(n):
#     y = int(input())
#     arr = list(map(int, input().split()))
#     operations = []
#     for _ in range(40):
#         if all(i == 0 for i in arr):
#             break
#         x = max(arr)
#         operations.append(x)
#         arr = [abs(i - x) for i in arr]
#     if all(i == 0 for i in arr):
#         result.append(str(len(operations)))
#         result.append(" ".join(map(str, operations)))
#     else:
#         result.append("-1")
# for res in result:
#     print(res)
import sys

input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1
results = []

for _ in range(t):
    n = int(data[idx])
    idx += 1
    arr = list(map(int, data[idx:idx + n]))
    idx += n

    # We will use a set to keep track of unique values in the array
    unique_values = set(arr)

    operations = []
    while unique_values and len(operations) < 40:
        max_val = max(unique_values)
        operations.append(max_val)
        new_values = {abs(val - max_val) for val in unique_values}
        unique_values = new_values

    if len(operations) > 40:
        results.append("Impossible")
    else:
        results.append(f"{len(operations)}\n" + " ".join(map(str, operations)))

print("\n".join(results))
