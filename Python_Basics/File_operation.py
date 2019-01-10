# Read all the contents
with open('filename.txt') as file_object:
    contents = file_object.read()
    print(contents)

# With relative path
# On MacOS/Linux
# with open('parent_dir/filename.txt') as file_object:
# On Windows
# with open('parent_dir\filename.txt') as file_object:

# With absolute path
# On MacOS/Linux
# file_path = '/.../parent_dir/filename.txt'
# with open(file_path) as file_object:
# On Windows
# file_path = 'C:\...\parent_dir\filename.txt'
# with open(file_path) as file_object:

# Read line by line
filename = 'filename.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Store lines in list
filename = 'filename.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# Write to file
filename = 'write_file.txt'
with open(filename, 'w') as file_object:
    file_object.write("Test write to file")

# read mode ('r')
# write mode ('w')
# append mode ('a')
# read and write mode ('r+')
# If omit the mode argument, Python opens the file in read-only mode by default.
# Open function will create the file if not exist.
# 'w' mode will erase the file if it already exists.
