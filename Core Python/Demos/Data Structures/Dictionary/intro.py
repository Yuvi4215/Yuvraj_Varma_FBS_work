### dictionary

key={"name": "isName", 1:"jhghj", 1.1:"vbhjk","name":654, True:"is True",str:"string", False:"is false"}

print(key[1])
print(key[1.1])
print(key[True])
print(key[False])
print(key[str])
print(key["name"])

print(id(key["name"]))
print(key["name"])
key["name"]= "new value"
print(id(key["name"]))
print(key["name"])