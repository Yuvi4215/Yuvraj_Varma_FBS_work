# ### 1st demo for file handling
# fp= open("C:/Users/Ajay Varma/Desktop/banking_management_system.txt", "r")
fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_1.txt", "a")

file_content = fp.write("\nNext Line containt.\tAnd Append at end.")
print(file_content)
fp.close()