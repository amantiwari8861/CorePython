
# Loops : 
# for 
# while

# numbers=range(10)
# range(start,end,step)
# numbers=range(3,10)
# print(numbers)
# print(type(numbers))

# for num in range(10):
#     print(num,"Hello Aman Sir")

# for num in range(2,10):
#     print(num,"Hello Aman Sir")

# initialization (2) ; condition (2<100); inc/dec (2+=3)

# for num in range(2,100,3): 
#     print(num,"Hello Aman Sir")


# for num in range(10,1,-1): 
#     print(num,"Hello Aman Sir")

# 1-100 : total ?

# total=0
# for i in range(1,11):
#     total=total+i
# print(total)

"""
    psuedocode(dry-run)

    Step 1: i=1,total=0
            i<11  -> 1<11 True
            total=total+i
            total=0+1 -> 1

    Step 2: i=2,total=1
            2<11 T
            total=1+2 => 3

    .
    .
    Step 10: i=10,total=45
            10<11 T
            total=45+10 => 55
        
    Step 11: i=11,total=55
            11<11 False 
            Loop terminated

"""

# Write a program in python to read 10 numbers from keyboard and find their total and average.  
# Test Data :
# Input the 10 numbers :
# Number-1 :2
# ...
# Number-10 :2
# Expected Output :
# The total of 10 no is : 55
# The Average is : 5.500000


# total=0
# for i in range(1,6):
#     temp=int(input("Enter a number :"))
#     total+=temp

# print("The total is ",total)

# while 
# i=1
# while i<=10:
#     print("i=",i)
#     i+=1
    
# i=100
# while i>=0:
#     print("i=",i)
#     i-=5

num=int(input("enter a number :"))
temp=num
""" rem=num%10 # 3
sum=sum+rem**3 # 27
num=num//10 # 15

rem=num%10 # 5
sum=sum+rem**3 # 27+125
num=num//10 # 1

rem=num%10 # 1
sum=sum+rem**3 # 27+125+1 => 153
num=num//10 # 0
 """

sum=0
while num>0:
    rem=num%10 
    sum+=(rem**3) 
    num=num//10 

if sum==temp:
    print("Armstrong No.")
else:
    print("not a armstrong no.")

# 1634 -> 1^4