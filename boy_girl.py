x = input()
y = x.lower()
if len(y) <=100 :
    z = set(y)
    if len(z)%2 == 0 :
        print("CHAT WITH HER!")
    else :
        print("IGNORE HIM!")

