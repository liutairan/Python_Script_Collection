def title_string(input_str):
    return input_str.title()

class AddOne():
    """Add one to each input number"""
    def __init__(self):
        self.saved_data = []

    def store_data(self, new_input):
        self.saved_data.append([new_input, new_input+1])
