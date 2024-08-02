# 5+4 here + is an operator  and 5,4 is operand
"""
    unary : (only single operand is required) 
    binary : (2 operand is required)
    ternary : (3 operand is required)
    misc : in,is
"""

# arithematic opeartor eg. +,-,*,/,%,**,//

# num=10+15
# print("10+15 :",num)
# num=100-15
# print("100-15 :",num)
# num=10*15
# print("10*15 :",num)
# num=100/15
# print("100/15 :",num)
# num=100//15
# print("100//15 :",num)

# print(27%4)
# print(14%2)
# print(1%10)
# print(15%10)

# print(2**7)
# print(2.5**2)

# relational operator eg . <,>,<=,>=,==,!=

# print("10<20 :",10<20)
# print("10>20 :",10>20)
# print("100>20 :",100>20)
# print("10<=20 :",10<=20)
# print("10<=10 :",10<=10)
# print("10>=20 :",10>=20)
# print("10>=10 :",10>=10)
# print("10==20 :",10==20)
# print("10==10 :",10==10)
# print(10!=10)
# print(20!=10)

# logical operator eg. and,or,not

# print(10>20  and 100<50) # False and False 
# print(10>20  and 10<50 ) # False and True
# print(100>20 and 100<50) # True and False
# print(100>20 and 10<50 ) # True and True

# print("10>20  or 100<50 :",10>20  or 100<50) # False and False 
# print("10>20  or 10<50 :",10>20  or 10<50 ) # False and True
# print("100>20 or 100<50 :",100>20 or 100<50) # True and False
# print("100>20 or 10<50 :",100>20 or 10<50 ) # True and True

# print(not 10>20)
# print(not 100>20)

# assignment operator eg. =,+=,-=,*=,/=,%= etc.

# num=10
# num+1
# num=num+1
# num+=1
# num+=50
# print("num=",num)


# bitwise operator eg. &,|,~,<<,>>,^

# Bitwise and (&)
# 97    -> 01100001
# 53    -> 00110101
# 97&53 -> 00100001 ->  1*2^5 + 1*2^0 => 33 Ans.

# print(97&53)

# Bitwise or (|)
# 97    -> 01100001
# 53    -> 00110101
# 97|53 -> 01110101 => 117 Ans.

# print(97|53)

# Bitwise XOR (^)
# 97    -> 01100001
# 53    -> 00110101
# 97^53 -> 01010100

# print(97^53)

# print(~10) # 10 + 1 => 11 => -11
# print(~-10)  # -10+1 => -9 => 9


# left shift << 
# 97    -> 01100001
# 97<<1 -> 11000010 # 97*2 => 
# 97<<2 -> 10000100 # 97*2*2 => 
# print(97<<1)
# print(97<<2)

# print(3<<1)
# print(3<<2)
# print(3<<3)
# print(3<<4)

# right shift >>
# 97    -> 01100001
# 97>>1 -> 00110000 => 97/2 => 48
# 97>>2 -> 
# print(97>>1)
# print(97>>2)

# print(97>>1)
# print(97>>2)
# print(97>>3)
# print(97>>4)


# ternary or conditional operator
# num1,num2=100,20

# max=num1 if num1>num2 else num2
# print("Max =",max)

# min=num1 if num1<num2 else num2
# print("Min =",min)

# print("A" in "Aman")
# print("Aman" == "Aman")

# membership operator(in)
# nums=[10,20,30]
# print(10 in nums)
# print(40 in nums)
# print(40 not in nums)

# identity operator (is)
name1="AMan"
name2="AMan"
print(name1 is name2)
print(name1 is not name2)