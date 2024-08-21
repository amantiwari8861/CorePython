# when a function call it itself

# def printNum(num):
#     print("num=",num)
#     if num<10:
#         printNum(num+1)
# print("before calling")
# printNum(1)
# print("after calling")


# def printNum(num,stop):
#     print("num=",num)
#     if num<stop:
#         printNum(num+1,stop)
# print("before calling")
# printNum(1,int(input("enter stop no:")))
# print("after calling")


# def printNum(num):
#     print("num=",num)
#     if num==5:
#         return
#     if num<10:
#         printNum(num+1)

# print("before calling")
# printNum(1)
# print("after calling")


# 5 -> 5*4*3*2*1

# def fact(num):
#     if num==0 or num==1: # Base condition
#         return 1
#     else:
#         return num*fact(num-1)

# result=fact(int(input("enter number:")))
# print("the factorial is",result)

def testTree(num):
    if num>0: # Base condition
        print(num,end=" ")
        testTree(num-1)
        testTree(num-1)
testTree(3)
