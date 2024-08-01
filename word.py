import string
s = input()
count=0
count1=0
for i in s:
    if i in string.ascii_uppercase:
        count = count+1
    else:
        count1=count1+1
if count > count1:
    print(s.upper())
elif count < count1:
    print(s.lower())
else :
    print(s.lower())
