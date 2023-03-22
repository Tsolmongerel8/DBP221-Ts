'''
Bodlogo #1
'''
def is_palindrome(value):
    value_str = str(value)
    return value_str == value_str[::-1]

print(is_palindrome(121))  
print(is_palindrome(123))  
print(is_palindrome(11))   
print(is_palindrome(1))
'''
Bodlogo #2
'''
def count_upper_lower(lst):
    upper_count = 0
    lower_count = 0
    for item in lst:
        for char in str(item):
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
    return upper_count, lower_count
'''
Bodlogo #3
'''
def list_product(lst):
    product = 1
    for item in lst:
        product *= item
    return product
lst = [1, 2, 3, 4, 5]
print(list_product(lst))
'''
Bodlogo #4
'''
def factorial(num):
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))
'''
Bodlogo #5
'''
def reverse_list(lst):
    return lst[::-1]
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
'''
bodlogo #6
'''
def list_sum(lst):
    return sum(lst)
lst = [1, 2, 3, 4, 5]
print(list_sum(lst))
'''
bodlogo #7
'''

def remove_duplicates(lst):
    return list(set(lst))
lst = [1, 2, 2, 3, 4, 4, 4, 5]
print(remove_duplicates(lst))
'''
bodlogo #8
'''
def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)
print(max_of_three(10, 20, 30))