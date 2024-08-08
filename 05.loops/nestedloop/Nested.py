import time
# for i in range(1,11):
#     print("Chapter",i)
#     for j in range(1,6):
#         print("\tSection",j,end="\n")
#         for k in range(1,4):
#             print("\t\tpara",k,end="\n")
#         # print()
#     print()

# for i in range(5):
#     for j in range(7):
#         print("    i=",i,"j=",j,end="")
#         time.sleep(1)
#     print()
#     time.sleep(3)

# for i in range(5):
#     for j in range(8):
#         print("*",end="")
#         time.sleep(1)
#     print()
#     time.sleep(3)

# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(5):
#     for j in range(5,i,-1):
#         print("*",end="")
#     print()

#     *
#    **
#   ***
#  ****
# *****

for i in range(5):
    for sp in range(4,i,-1):
        print(" ",end="")
    for star in range(i+1):
        print("*",end="")
    time.sleep(1)
    print()