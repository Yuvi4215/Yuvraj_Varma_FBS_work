### writePlus(w+) mode


fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_2.txt", "w+")

print(f"cursor when file open : {fp.tell()}")

fp.write("AAA\nBBB\nCCC\nDDD\nEEE")

print(f"cursor after write : {fp.tell()}")

fp.seek(0, 0)
print(f"cursor after seek : {fp.tell()}")

fp.write("added")
print(f"cursor write : {fp.tell()}")

content = fp.read()
print(content)
print(f"cursor after read : {fp.tell()}")
fp.close()
