person = {
    "name": "Avi",
    "age": 19,
    "city": "Lucknow"
}
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
person["email"] = "avi.rawat0019@gmail.com"
print("Updated dictionary with email:", person)
person["age"] = 20
print("Updated dictionary with modified age:", person)
if "city" in person:
    print("Key 'city' exists in the dictionary")

keys = person.keys()
values = person.values()
print("Keys:", list(keys))
print("Values:", list(values))
