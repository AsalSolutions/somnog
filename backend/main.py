

users = {
    "id":1,
    "name":"Hassan",
    "age":29,
    "location":"Istanbul",
    "address":"Serdivan"

}
userAge = {"age":3000}
print(users.get("name"))
print(users.keys()) # lists keys of the dict

print(users.items()) # prints items in a group 
print(users.values()) # prints only values of the dict
print(users.pop("age"))
print(users.items()) # prints items in a group 
# newUsers = users.copy()
# print(users.clear())
users.update(userAge)
# print(users.__contains__("names"))


# List
listUsers = [124,'Hassan','Hassan''district',False,3,50]

print(listUsers.append("Newd"))

