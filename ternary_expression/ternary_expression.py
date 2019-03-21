# Grammer: <expression1> if <condition> else <expression2>

age = 15
print('kid' if age < 18 else 'adult')

age = 14
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')


from pprint import pprint

pprint('expression_1') if pprint('condition_1') else \
    pprint('expression_2') if pprint('condition_2') else pprint('expression_3')