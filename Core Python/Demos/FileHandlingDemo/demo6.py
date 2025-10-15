### AppendPlus(a+)

fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_3.txt", "a+")

print(f"cursor when file open : {fp.tell()}")

fp.write("\nAAA\nBBB\nCCC\nDDD\nEEE")

print(f"cursor after write : {fp.tell()}")

fp.seek(0, 0)
print(f"cursor after seek : {fp.tell()}")

fp.write("\nadded")
print(f"cursor write : {fp.tell()}")
fp.seek(0, 0)
content = fp.read()
print(content)
print(f"cursor after read : {fp.tell()}")
fp.close()