# nums={10,20,89,10,20,56,10}
# # list -> duplicate values,indexing,ordering allowed

# print(type(nums))
# print(nums)
# # print(nums[0]) # error

# nums.add(78)
# print(nums)


# names={"Aman","Naman","Raman","Aman","AMAN"}
# print(names)

basket1={"Apple","mango","cucumber"}
basket2={"cucumber","potato","radish"}

# print(basket1.difference(basket2)) # A-B
# print(basket2.difference(basket1)) # B-A
# print(basket1.union(basket2))
print(basket1.issuperset(basket2))
# print(len(basket1))

# basket1.update({"banana","Strawberry"})
# print(basket1)
