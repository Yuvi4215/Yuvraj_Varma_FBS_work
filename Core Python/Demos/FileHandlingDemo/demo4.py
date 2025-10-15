### Read plus mode(r+)
fp = open(
    "Core Python/Demos/FileHandlingDemo/fileHandlingDemo_1.txt", "r+"
)  # opening file in readPus mode
print(f"Cursor Pointer is at :: {fp.tell()}")  # tell cursor position
content = fp.read()
print(content)
print(f"Cursor Pointer is at :: {fp.tell()}")  # tell cursor position

fp.write("\nThis line is added.")  # add containt
print(f"Cursor Pointer is at :: {fp.tell()}")  # tell cursor position

fp.seek(5,0)    # take cursor to seek(index of elements to skip, 0-start: 1-current: 2-end)
print(f"Cursor Pointer is at :: {fp.tell()}")  # tell cursor position

content = fp.read()
print(content, "------------------")

fp.close()
