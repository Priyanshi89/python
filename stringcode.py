x = int(input())
if x <=1000 and x>=1:

    for i in range(x):
        count = 0
        a = input()
        b = a.lower()
        if b[0] != "c":
            count = count + 1  
        if b[1] != "o":
            count = count + 1
        if b[2] != "d":
            count = count+1
        if b[3] != "e":
            count = count+1
        if b[4] != "f":
            count = count+1
        if b[5] != "o":
            count = count+1
        if b[6] != "r":
            count = count+1
        if b[7] != "c":
            count = count+1
        if b[8] != "e":
            count = count+1
        if b[9] != "s":
            count = count+1
        print(count)
   