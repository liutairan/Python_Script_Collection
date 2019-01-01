# Exit while loop
prompt = "\nInput: "
prompt += "\n(Enter 'quit' when you want to quit.) "
while True:
    input_str = input(prompt)
    if input_str == 'quit':
        break
    else:
        print(input_str)

# Return to the beginning of the loop, but not exit the while loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
