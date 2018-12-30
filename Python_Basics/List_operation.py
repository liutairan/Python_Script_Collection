l1 = ['test1', 'test2', 'test3', 'test4', 'test5']

# First element
print(l1[0])
# Last element
print(l1[-1])
# Add element
l1.append('test_new1')
print(l1)

# Insert
l1.insert(0, 'test_new2')
print(l1)

# Remove
del l1[0]
print(l1)

# Remove with pop
popped_element = l1.pop()
print(l1)
print(popped_element)

# Pop item from position
popped_element_another = l1.pop(0)
print(l1)
print(popped_element_another)

# Remove item by value
l1.remove('test3')
print(l1)

# Sort
l2 = ['bfaf', 'ehluibl', 'hjo;ij', 'adfas', 'caasg']
l2.sort()
print(l2)
# sort will actually change the order

# sorted
l3 = ['bfaf', 'ehluibl', 'hjo;ij', 'adfas', 'caasg']
print(sorted(l3))
print(l3)
# sorted will not actually change the order

# reverse
l4 = ['bfaf', 'ehluibl', 'hjo;ij', 'adfas', 'caasg']
l4.reverse()
print(l4)

# length
l5 = [4,3,5,1,2]
print(len(l5))

# Loop the list
l6 = ['apple', 'banana', 'grape', 'mango']
for fruit in l6:
    print(fruit)

# Numerical List
for i in range(1,5):
    print(i)

# Make list of numbers:
nums1 = list(range(2,6))
print(nums1)
nums2 = list(range(2,11,2))
print(nums2)

# Min, max, sum
print(min(nums2))
print(max(nums2))
print(sum(nums2))

# List comprehension
squares = [value**2 for value in range(10,20)]
print(squares)

# Slice
l7 = list(range(10,20))
print(l7)
print(l7[1:5])
print(l7[:5])
print(l7[5:])
print(l7[-3:])

# Copy a list
l8 = list(range(10,20))
l8_copy = l8[:]
print(l8)
print(l8_copy)
l8.pop()
print(l8)
print(l8_copy)

# false copy
l9 = list(range(10,20))
l9_copy = l9
print(l9)
print(l9_copy)
l9.pop()
print(l9)
print(l9_copy)
