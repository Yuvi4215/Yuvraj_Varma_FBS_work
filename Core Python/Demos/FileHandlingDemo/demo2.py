code_containt="""
### 1st demo for file handling(Reading)
# fp= open("C:/Users/Ajay Varma/Desktop/banking_management_system.txt", "r")
fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_1.txt", "r")
file_content = fp.read()
print(file_content)

### 1st demo for file handling(Writing)
fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_1.txt", "w")
file_content = fp.write(code_containt)
print(file_content)
"""
fp = open("Core Python/Demos/FileHandlingDemo/fileHandlingDemo_1.txt", "w")
file_content = fp.write(code_containt)
print(file_content)
fp.close()