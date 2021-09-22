# 集合是不同元素的无序集合
animals = {'cat', 'dog'}
print('cat' in animals)  # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')  # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))  # Number of elements in a set; prints "3"
animals.add('cat')  # Adding an element that is already in the set does nothing
print(len(animals))  # Prints "3"
animals.remove('cat')  # Remove an element from a set
print(len(animals))  # Prints "2"

# 循环(Loops): 遍历集合的语法与遍历列表的语法相同；但是，由于集合是无序的，因此不能假设访问集合元素的顺序：
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: fish", "#2: dog", "#3: cat"

# 集合推导式(Set comprehensions): 就像列表和字典一样，我们可以很容易地使用集合理解来构造集合
from math import sqrt

nums = {int(sqrt(x)) for x in range(30)}
print(nums)
# Prints "{0, 1, 2, 3, 4, 5}"
