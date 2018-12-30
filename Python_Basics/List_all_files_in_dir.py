import os

# List all the files in current directory
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)

# List all the files in parent directory
for root, dirs, files in os.walk(".."):
    for filename in files:
        print(filename)

# List all the files in an absolute path
pathTBL = "/.../"
for root, dirs, files in os.walk(pathTBL):
    for filename in files:
        print(filename)
