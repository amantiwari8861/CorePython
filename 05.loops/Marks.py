# marks=[98,97,95,45,33,91]
# # index : 0 - 5

# for i in range(len(marks)):
#     print("Marks[",i,"]=",marks[i],sep="")

# marks=[]
# temp=1
# num=65
# while temp!=0:
#     temp=int(input(f"enter marks of subject {chr(num)}  :"))
#     if temp==0:
#         break
#     marks.append(temp)
#     num+=1

# print("the marks are",marks)

# print(f"temp ki value {temp} hai and num ki value {num} hai")

# print(" num=%d  "%num)

# print(" the number is %f "%12.564768)
# print(" the number is %.2f "%12.564768)

# print("1 Hello")
# print("10 Hello")
# print("100 Hello")
# print("1000 Hello")


# print("|%4s| %s"%(1,"Hello"))
# print("|%4s| %s"%(10,"Hello"))
# print("|%4s| %s"%(100,"Hello"))
# print("|%4s| %s"%(1000,"Hello"))

# print("|%-4s| %s"%(1,"Hello"))
# print("|%-4s| %s"%(10,"Hello"))
# print("|%-4s| %s"%(100,"Hello"))
# print("|%-4s| %s"%(1000,"Hello"))

column_names=("Full Name","Math","science","SST","Hindi","English")
stu1=("Aman",98,97,96,95,99)
stu2=("Aman Tiwari",98,97,96,95,99)
stu3=("Chinnu swami muttu ",98,97,96,95,99)
stu4=("Aman 3",98,97,96,95,99)

print(" %-20s %-7s %7s %7s %7s %7s"%column_names)
print(" %-20s %-7s %7s %7s %7s %7s"%stu1)
print(" %-20s %-7s %7s %7s %7s %7s"%stu2)
print(" %-20s %-7s %7s %7s %7s %7s"%stu3)
print(" %-20s %-7s %7s %7s %7s %7s"%stu4)

