# Python包含几种内置的容器类型：列表、字典、集合和元组
xs = [3, 1, 2]  # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])  # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'  # Lists can contain elements of different types
print(xs)  # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)  # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()  # Remove and return the last element of the list
print(x, xs)  # Prints "bar [3, 1, 'foo']"

nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"

# (循环)Loops: 你可以循环遍历列表的元素，如下所示：
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.

# 如果要访问循环体内每个元素的索引，请使用内置的 enumerate 函数：
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

# 列表推导式(List comprehensions): 编程时，我们经常想要将一种数据转换为另一种数据。
# 举个简单的例子，思考以下计算平方数的代码：
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]

# 你可以使用 列表推导式 使这段代码更简单:
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]

# 列表推导还可以包含条件：
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"
