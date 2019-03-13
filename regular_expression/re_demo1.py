import re
import inspect

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)

if match:
    print('found is: ', match.group())
else:
    print('did not find')

match = re.search(r'iii', 'piiig')
# result: "iii"

if match:
    print(match.group())

match = re.search(r'igs', 'piiig')
# result: "None"

if match:
    print(match.group())

# . = any char but \n
match = re.search(r'..g', 'piiig')
# result: iig

if match:
    print(match.group())

# \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')
# result: 123

if match:
    print(match.group())

match = re.search(r'\w\w\w', '@@abcd!!')
# result: abc

if match:
    print(match.group())


#############################
#   Repetition Examples
#############################
match = re.search(r'pi+', 'piiig')
if match:
    print(match.group())
# result: piii

match = re.search(r'i+', 'piigiiii')
if match:
    print('#54')
    print(match.group())
# result: ii

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace
def match_result(result): 
    print(inspect.currentframe().f_back.f_lineno)
    if result:
        print(match.group())
    else:
        print("Not found")

match = re.search(r'\d\s*\d\s*\d', 'xx1 2    3xx')
match_result(match)

# re.match() checks for a match only at the beginning of the string, 
# while re.search() checks for a match anywhere in the string (this is what Perl does by default).

## ^ = match the start of string, so this failes:
match = re.search(r'^b\w+', 'foobar')
match_result(match)

match = re.search(r'o\w+', 'foobar')
match_result(match)

## Emails Example
# w会匹配[a-zA-Z_], 即大小写字母a-z和下划线
mail = 'purple alice-__b__@_google_.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', mail)
match_result(match)

def get_line_num():
    print('You are in {}'.format(inspect.currentframe().f_back.f_lineno))

str = 'purple alice@google.com, blash monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
get_line_num()
for email in emails:
    print(email)
