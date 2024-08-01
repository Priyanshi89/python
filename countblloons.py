x = int(input())
result= []
for i in range(x):
        y = int(input())
        s = input()

        set_of_problems = set()
        balloons=0
        for i in s:
            if i not in set_of_problems:
                set_of_problems.add(i)
                balloons+=2
            else:
                balloons+=1
        result.append(balloons)
for i in result:
     print(i)

        
        
          
            
               
            