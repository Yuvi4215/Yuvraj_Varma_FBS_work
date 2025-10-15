fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_4.txt", "a+")

print(f"cursor when file open : {fp.tell()}")

fp.seek(0,0)
print(f"cursor after seek: {fp.tell()}")
fp.write("\n123")