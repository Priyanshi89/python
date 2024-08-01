x = int(input( ))
if 1 <= x <= 10000:

    for i in range(x):
        #count = 0
        a, b = map(int, input().split())
        # while a % b != 0:
        #     a = a+1
        #     count = count+1
        # print(count)
        reminder = a % b
        if reminder == 0:
            print(0)
        else:
            moves = b - reminder
            print(moves)
    
