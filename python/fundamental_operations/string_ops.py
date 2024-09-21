# Printing array of strings as a list using generator expression
str_arr = ['Hello', 'World']
print(*[f'- {str_item}' for str_item in str_arr], sep='\n')
# Output: - Hello
#         - World

# Format string with join method and generator expression
str_arr = ['Hello', 'World']
print('\n'.join([f'- {str_item}' for str_item in str_arr]))


# Format string with f-string
name = 'John'
age = 30
print(f'My name is {name} and I am {age} years old.')
# Output: My name is John and I am 30 years old.


# Format string with format method
name = 'John'
age = 30
print('My name is {} and I am {} years old.'.format(name, age))
# Output: My name is John and I am 30 years old.


# Format string with format method and positional arguments
name = 'John'
age = 30
print('My name is {first} and I am {second} years old.'.format(first=name, second=age))
# Output: My name is John and I am 30 years old.


# Format string with % operator
name = 'John'
age = 30
print('My name is %s and I am %d years old.' % (name, age))
# Output: My name is John and I am 30 years old.

# Checking if a string starts with/ends with a specific substring
urls = ['https://www.google.com', 'https://www.facebook.com', 'https://www.twitter.com',
        'https://www.linkedin.com', 'https://www.instagram.com', 'https://www.pinterest.com']
for url in urls:
    if url.startswith('https://www.'):
        print(f'{url} starts with https://www.')
    if url.endswith('.com'):
        print(f'{url} ends with .com')
# Output: https://www.google.com starts with https://www.
#         https://www.google.com ends with .com
#         https://www.facebook.com starts with https://www.
#         https://www.facebook.com ends with .com
#         https://www.twitter.com starts with https://www.
#         https://www.twitter.com ends with .com
#         https://www.linkedin.com starts with https://www.
#         https://www.linkedin.com ends with .com
#         https://www.instagram.com starts with https://www.
#         https://www.instagram.com ends with .com
#         https://www.pinterest.com starts with https://www.
#         https://www.pinterest.com ends with .com

# Checking if a string contains a specific substring
string = 'Hello, World!'
if 'World' in string:
    print('World is present in the string {string}.'.format(string=string))
# Output: World is present in the string Hello, World!.

# Joining strings using join method
str_arr = ['Joshua', 'David', 'John']
print(', '.join(str_arr))
# Output: Joshua, David, John

# Splitting a string into a list of strings
string = 'Joshua, David, John'
print(string.split(', '))
# Output: ['Joshua', 'David', 'John']

# Replacing a substring with another substring
string = 'Joshua, David, John'
print(string.replace('David', 'Doe'))
# Output: Joshua, Doe, John
