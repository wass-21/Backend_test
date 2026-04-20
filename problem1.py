import math
def multiple_number(n):
    arr = []
    if type(n) is not int :
        return "sorry you should put a number"
    
    if n == 0 : 
        return "Sorry 0 is not acceptable"
    
    if n < 0 : 
        return "Sorry your number should be positive"
    
    for i in range(1,n + 1):
        arr.append(i)
    
    x = math.lcm(*arr) #Return the least common multiple of the specified integer arguments

    return x


print(multiple_number(-5))