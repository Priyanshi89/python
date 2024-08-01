# n = int(input())
# result = []
# for i in range(n):
#     counts = 0
#     y = int(input())
#     li = list(map(str, input().split()))
#     for j in li:
#         counts = li.count(j)
#         if counts >= 3:
#             k = j
#         elif all(li.count(i) < 3 for i in li):
#             k = -1
#         result.append(k)
# for i in result:
#     print(i)
n = int(input())
result = []

for _ in range(n):
    y = int(input())  # Read the length of the array (though it's not used in further calculations)
    li = list(map(int, input().split()))  # Read the array elements
    
    counts = {}
    k = -1  # Default value if no element appears at least 3 times
    
    # Count occurrences of each element
    for j in li:
        if j in counts:
            counts[j] += 1
        else:
            counts[j] = 1
        
        # Check if the count of the element reaches 3
        if counts[j] == 3:
            k = j
            break  # Early exit as we found an element that appears at least 3 times
    
    result.append(k)

# Print all results
for i in result:
    print(i)
