### Data Type - List 

a = [10, 'abbas',  2.65]  # Creating a list

print(a)  # Output: [10, 'abbas', 2.65]
print(type(a))  # Output: <class 'list'>


#Example 2

var = f = ["apple",'banana','orange','mango']
 
var= f[2]


print(var)



### Function & Methods of List

v = [10, 'abbas',  265.8] 

v.index('abbas')  # Output: 1
v.append('hello')  # v becomes [10, 'abbas', 265.8, 'hello']
v.remove(10)  # v becomes ['abbas', 265.8, '    hello']
v.insert(1, 'world')  # v becomes ['abbas', 'world', 265.8, 'hello']
v.pop()  # Output: 'hello', v becomes ['abbas', 'world', 265.8]
len(v)  # Output: Length of the list
v.append(100)  # v becomes ['abbas', 'world', 265.8, 100]
v.insert(0, 'start')  # v becomes ['start', 'abbas', 'world', 265.8, 100]
v.remove('world')  # v becomes ['start', 'abbas', 265.                  
v.reverse()  # Reverses the list    

