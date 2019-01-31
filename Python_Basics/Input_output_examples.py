# Formatted string literals
var1 = 10
var2 = 'A string'
result1 = f'{var1}, {var2}'
result2 = F'{var1}, {var2}'
print(result1)
print(result2)
# 10, A string
# 10, A string

# Passing an integer after the ':' will cause that field
# to be a minimum number of characters wide.
# This is useful for making columns line up.
var3 = 1_234 # This is equal to 1234
var4 = 2_468
var5 = var3/var4
result3 = 'var3 is {:-5}, var5 is {:2.2%}'.format(var3,var5)
print(result3)
# var3 is  1234, var5 is 50.00%

# The str() function is meant to return representations
# of values which are fairly human-readable,
# while repr() is meant to generate representations
# which can be read by the interpreter
s1 = 'Hello world'
print(str(s1))
print(repr(s1))
print(repr((10,20,('String 1','String 2'))))

# Modifiers can be used to convert the value before it is formatted.
# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()
var6 = 'Test String'
print(f'{var6}')
print(f'{var6!r}')

# String format() method
print('{0}, {1}'.format('para1','para2'))
print('{1}, {0}'.format('para1','para2'))
print('{field1}, {field2}'.format(field1='para1',field2='para2'))
print('{0}, {1}, {field3}'.format('para1','para2', field3='para3'))
dict_var1 = {'field1': 111, 'field2': 222, 'field3': 333}
print('field1: {0[field1]:d}; field2: {0[field2]:d}; '
      'field3: {0[field3]:d}'.format(dict_var1))
print('field1: {field1:d}; field2: {field2:d}; field3: {field3:d}'.format(**dict_var1))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# Manual string formatting
