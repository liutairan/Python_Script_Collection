# Passing an Arbitrary Number of Arguments
def print_parameters1(*arguments):
    # The asterisk tells Python to make an empty
    #     tuple with name arguments which packs
    #     whatever type of values it receives
    #     into this tuple.
    print(arguments)

print_parameters1('para1')
print_parameters1('para1', 'para2', 'para3')

# Mixing Positional and Arbitrary Arguments
def print_parameters2(para1, *arguments):
    # Python matches positional and keyword
    #     arguments first and then collects
    #     any remaining arguments in the final
    #     parameter.
    print(para1)
    print(arguments)

print_parameters2('para1', 'para2')
print_parameters2('para1', 'para2', 'para3')


# Using Arbitrary Keyword Arguments
def construct_dict(para1, para2, **other_paras):
    para_dict = {}
    para_dict['field1'] = para1
    para_dict['field2'] = para2
    for key, value in other_paras.items():
        para_dict[key] = value
    return para_dict

para_dict = construct_dict('para1', 'para2',
                           field3='para3',
                           field4='para4')
print(para_dict)
