
# Decorator
def My_Decorator(func) :
    
    def arrangers(*varss):

        print("*******" * 10)

        func(*varss)
        
        # print("*******" * 10)

    return arrangers 

# function
@My_Decorator
def Getsum(*vars) : 

    sum = 0

    for num in vars:
        sum += num
    return sum  


# generator
def gen(x,y,z):

    print(x+y)
    yield 1

    print(z+y)
    yield 2

    print(x+z)
    yield 3

   



print(Getsum(1,2))