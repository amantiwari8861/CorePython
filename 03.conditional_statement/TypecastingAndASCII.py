# ASCII -> American standard code for information interchange

# a -> 97 -> 1100001
# z -> 122 

# A -> 65
# Z -> 90

# 0 -> 48
# 9 -> 57

# print(ord('A'))

alphabet=input("enter any alphabet :")

if len(alphabet)>1:
    print("invalid !")
else:
    ch=ord(alphabet)
    if (ch>=65 and ch<=90 ) or (ch>=97  and ch<=122) :
        print("The alphabet is ",alphabet)
    else:
        print("any other character")

