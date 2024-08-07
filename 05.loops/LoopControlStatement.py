import math
# Prime No : ?
isPrime=True
num=int(input("enter a number :"))

if num>0:
    for i in range(2,int(math.sqrt(num))+1):
        # if num%i==0:
        #     print(num,i,"se perfectly kat gaya (factor)")
        # else:
        #     print(num,i,"se perfectly nahi kata (not a factor)")
        if num%i==0:
            isPrime=False
            print(num,"not a prime no bcz it is divisible by",i)
            # break
        else:
            print(num," is a prime no bcz it is divisible by",i)

    if isPrime:
        print(num," is a prime no.")


# 36 ->  1,2,3,4,6

# sqrt(36) => 6
# sqrt(24)