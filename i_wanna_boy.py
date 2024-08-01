x = int(input())
abc = set(map(int, input().split()[1:]))
xyz = set(map(int, input().split()[1:]))
combined_levels = set(list(abc) + list(xyz))



if len(combined_levels) == x:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
