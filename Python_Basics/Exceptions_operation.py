try:
    print(1/0)
except ZeroDivisionError:
    print("Zero in denominator")

# Code that depends on the try block executing successfully goes in the else block
print("Type in 2 numbers:")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Zero in denominator")
    else:
        print(answer)

# FileNotFoundError
filename = 'filename.txt'
try:
    with open(filename) as f_obj:
    contents = f_obj.read()
except FileNotFoundError:
    msg = filename + " does not exist."
    print(msg)
else:
    print(contents)
