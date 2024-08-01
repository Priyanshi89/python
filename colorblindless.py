x = int(input())
result = []
for i in range(x):
    y = int(input())
    li = list(map(str, input()))
    li1 = list(map(str, input()))
    
    
    identical = True
    
    for i in range(y):
        if li[i] == li1[i] or ((li[i]=="G" and li1[i]=="B") or (li[i]=="B" and li1[i]=="G")):
            identical = True
        else:
            identical = False
            break
            
    if identical:
        result.append("YES")
    else:
        result.append("NO")
for i in result :
    print(i)

        