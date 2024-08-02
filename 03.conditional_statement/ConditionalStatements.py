#  conditional statements eg. if,if-else,elif (ladder) ,nested 

# age=int(input("Enter age:"))

# if age>=18 : # true block
# #  print("u can vote!")
# #   print("congrats!")
#     print("great!")

# if age>=18:
#        print("u can vote!")
# else:
#     print("u can't vote!")

percentage=float(input("enter ur percentage :"))

# if percentage>80:
#     print("u got admission in DU")
# elif percentage>60:
#     print("u got admission in IPU")
# elif percentage>50:
#     print("u got admission in Amity")
# elif percentage>=33:
#     print("private university")
# else:
#     print("Repeat")


if percentage>80:
    print("u got admission in DU")
    if percentage==100:
        print("no fee will be charged")
    elif percentage>=95:
        print("u got 50K scholarship")
    # else:
    #     print("no scholarship")
elif percentage>60:
    print("u got admission in IPU")
elif percentage>50:
    print("u got admission in Amity")
elif percentage>=33:
    print("private university")
else:
    print("Repeat")

