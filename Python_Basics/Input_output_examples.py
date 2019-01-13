# Formatted string literals
var1 = 10
var2 = 'A string'
result1 = f'{var1}, {var2}'
result2 = F'{var1}, {var2}'
print(result1)
print(result2)
# 10, A string
# 10, A string

#
var3 = 1_234
var4 = 2_468
var5 = var3/var4
result3 = 'var3 is {:-5}, var5 is {:2.2%}'.format(var3,var5)
print(result3)
# var3 is  1234, var5 is 50.00%
