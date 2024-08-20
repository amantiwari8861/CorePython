
#functions : set of instructions which together performs a particular task
# 1. pre-defined
# 2. user-defines

# no argument no return type 
# no argument with return type 
# with argument no return type 
# with argument and return type
 
# reusability
# modularity
# decrease complexity
# increase readibility
# loose coupling

# coupling and cohesion

# print("Hello")

# res=pow(2,7)
# print("the result is ",res)

# no argument no return type
# def greet(): 
#     print("good evening Sir !!") # task of 10K lines
    # return 99999

# greet() # calling of greet function
# greet() # calling of greet function
# greet() # calling of greet function
# greet() # calling of greet function

# print(greet()) # None

# no argument with return type
def getPiValue():
    return 3.14

# res=getPiValue()
# print("result=",res)

# print(getPiValue())


# with argument no return type
# def VolumeOfSphere(r):
#     print("volume is :",4/3*getPiValue()*r**3)


# r=float(input("enter radius:"))
# VolumeOfSphere(r)


def powerFxn(base,power):
    result=1
    for i in range(power):
        result*=base
    return result

res=powerFxn(3,4)
print("3^4 is ",res)

b=float(input("enter base:"))
p=int(input("enter power:"))
res=powerFxn(b,p)
print(b,"^",p," is ",res)


# cylinder 




