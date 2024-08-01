# import string
# n = int(input())
# li = (input().lower())
# if n < 26 :
#     print("NO")
# else:

#     for i in range(n):
#         st = set(string.ascii_lowercase)
#         li1 = set(li)
#         if st.issubset(li1):
#             print("YES")
#         else:
#             print("NO")
import string

n = int(input())  
li = input().lower()  
if n < 26:
    print("NO")
else:

    alphabet_set = set(string.ascii_lowercase)

    
    input_set = set(li)

    
    if alphabet_set.issubset(input_set):
        print("YES")
    else:
        print("NO")

        