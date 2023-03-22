'''
Бодлого #1
'''
list1=['python', 'php', 'java']
print(list1[0])
'''
Бодлого #1.2
'''
list1=['python', 'php', 'java']
print(list1[1])
'''
Бодлого #1.3
'''
list1=['python', 'php', 'java']
print(list1[2])
'''
# Бодлого #2
# '''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for number in numbers:
    sum += number

print("Sum:", sum)
'''
Бодлого #3
'''
lst = [1, 2, 3, 4, 5]

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

result = product_of_list(lst)
print(result)
'''
Бодлого #4
'''
def sum_of_product(numbers):
    third = numbers[2]
    last = numbers[-1]
    product = third * last
    return product

numbers = [1, 2, 3, 4, 5]
result = sum_of_product(numbers)
print(result)
'''
Бодлого #5
'''
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = [1, 2, 3, 4, 5]
result = min_max(numbers)
print(result)
'''
Бодлого #6
'''
def count_same_start_end(strings):
    count = 0
    for string in strings:
        if len(string) >= 3 and string[0] == string[-1]:
            count += 1
    return count

strings = ['abdba', 'abcd', '121']
result = count_same_start_end(strings)
print(result)
'''
Бодлого #7
'''
def remove_duplicates(lst):
    return list(set(lst))

lst = ['abdba', 'abcd', '121', '121', 'abcd']
result = remove_duplicates(lst)
print(result)
'''
Бодлого #8
'''
def is_list_empty(lst):
    return len(lst) == 0

lst = []
result = is_list_empty(lst)
print(result)
'''
Бодлого #9
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = [x for i, x in enumerate(lst) if i not in [3, 5, 7]]
print(lst)
'''
Бодлого #10
'''
numbers = (1, 2, 3, 4, 5)
'''
Бодлого #11
'''
numbers = (1, 2, 3, 4, 5)
new_numbers = numbers + (6, 7, 8)
print(new_numbers)
'''
#Бодлого #12
'''
numbers = (1, 2, 3, 4, 5)
print(numbers[1])
print(numbers[3])
'''
Бодлого #13
'''
numbers = (1, 2, 3, 4, 5)
value = int(input("Enter a value to search for: "))
if value in numbers:
    print(f"{value} found in the tuple")
else:
    print(f"{value} not found in the tuple")
'''
Бодлого #14
'''
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)
'''
Бодлого #15
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
combined_set = set1.union(set2)
print(combined_set)
'''
Бодлого #16
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print(intersection_set)
'''
Бодлого #17
'''
numbers = {1, 2, 3, 4, 5}
length = len(numbers)
print(length)
'''
Бодлого #18
'''
numbers = {1, 2, 3, 4, 5}
value = int(input("Enter a value to remove: "))
if value in numbers:
    numbers.remove(value)
    print(numbers)
else:
    print(f"{value} not found in the set")
'''
Бодлого #19
'''
numbers = {1, 2, 3, 4, 5}
numbers.clear()
print(numbers)
'''
Бодлого #20
'''
numbers = {1, 2, 3, 4, 5}
del numbers
try:
    print(numbers)
except NameError:
    print("The set has been deleted.")
'''
Бодлого #21
'''
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sorted_dict = dict(sorted(numbers.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)
'''
Бодлого #22
'''
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
key = input("Enter a key to check: ")
if key in numbers:
    print(f"{key} is in the dictionary with value {numbers[key]}")
else:
    print(f"{key} is not in the dictionary")
'''
Бодлого #23
'''
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
value = int(input("Enter a value to check: "))
if value in numbers.values():
    print(f"{value} is in the dictionary")
else:
    print(f"{value} is not in the dictionary")
'''
Бодлого #24
'''
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for key, value in numbers.items():
    print(f"{key}: {value}")
'''
Бодлого #25
'''
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
dict1.update(dict2)
print(dict1)
'''
Бодлого #26
'''
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
dict1.update(dict2)
print(dict1)



