
x = input()
result = ""
skip = False

for i in range(len(x)):
    if skip:
        skip = False
        continue
    
    if x[i] == ".":
        result += "0"
    elif i < len(x) - 1 and x[i] == "-" and x[i + 1] == ".":
        result += "1"
        skip = True  
    elif i < len(x) - 1 and x[i] == "-" and x[i + 1] == "-":
        result += "2"
        skip = True  
    

print(result)
