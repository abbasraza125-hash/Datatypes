# Creating a tuple
a = (10, 'abbas', 2.65)

print(a)            # Output: (10, 'abbas', 2.65)
print(type(a))      # Output: <class 'tuple'>


#Example 2

f = ("apple", "banana", "orange", "mango")  

var = f[2]  # Accessing element at index 2

print(var)   # Output: orange


v = (10, 'abbas', 265.8)

# Accessing tuple elements and methods
print(v.index('abbas'))   # Output: 1
print(len(v))             # Output: 3
print(v.count(10))        # Output: 1



# You can also repeat tuples
v2 = v * 2
print(v2)  # Output: (10, 'abbas', 265.8, 'hello', 'world', 10, 'abbas', 265.8, 'hello', 'world')

# To reverse a tuple, use slicing
v_reversed = v[::-1]
print(v_reversed)  # Output: ('world', 'hello', 265.8, 'abbas', 10)
