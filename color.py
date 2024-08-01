n, m = map(int, input().split())

pic=[]
for i in range(n):
    row = input().split()
    pic.append(row)


    
colors = set(['C', 'M', 'Y'])
is_colored = False
for row in pic:
        for pixel in row:
            if pixel in colors:
                is_colored = True
                break
        if is_colored :
             break
if is_colored:
    print("#Color")
else:
    print("#Black&White")