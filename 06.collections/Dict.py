# aadharCard=["Ram",24,'M',"Shyam","Noida"]

# userDetails={}
# userDetails=dict()
# userDetails={"name":"Aman"}
# print(type(userDetails))
# print(userDetails)

aadharCard={
    "name":'Aman',
    "age":28,
    "mobileNo":8448179216,
    "skills":["java fullstack","MEAN","MERN","etc"],
    "address":{
        "city":"Noida",
        "country":"india",
        "pincode":201301
    },
    "ismarried":False,
    "height":5.6
}

# aadharCard["skills"].append("Python")

# print(aadharCard)
# print(aadharCard["age"])
# print(aadharCard["address"]["pincode"])
# aadharCard["name"]="Tarang"
# aadharCard.update({"name":"tarang"})
# aadharCard.update({"weight":72})

# for k in aadharCard:
#     # print(f"\t {k} : {aadharCard[k]}")
#     print(" %10s : %s"%(k,aadharCard[k]))


# for k,v in aadharCard.items():
#     print(k,":",v)

# for k,v in aadharCard.items():
#     if isinstance(v,dict):
#         print(k,":")
#         for k2,v2 in v.items():
#             print("\t",k2,":",v2)
#     else:
#         print(k,":",v)