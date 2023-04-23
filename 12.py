import hashlib

a = input("md5 pass : ")

str2hash = a


result = hashlib.md5(str2hash.encode())


print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())
