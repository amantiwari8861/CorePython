percentage=float(input("enter ur percentage :"))

# if percentage>=80 and percentage<=100:  # 
#     print("u got admission in DU")
    
# if 80<= percentage <=100:
#     print("u got admission in DU")

# result=10>20 and 40>30 and 50<100 and 100>40  
# print(result)


if percentage>=80 and percentage<=100:
    print("u got admission in DU")
    if percentage==100:
        print("no fee will be charged")
    if percentage>=95:
        print("u got 50K scholarship")
elif percentage>=60 and percentage<80:
    print("u got admission in IPU")
elif percentage>=50 and percentage<60:
    print("u got admission in Amity")
elif percentage>=33 and percentage<50:
    print("private university")
elif percentage>=0 and percentage<33:
    print("Repeat")
else:
    print("pls input valid percentage.")