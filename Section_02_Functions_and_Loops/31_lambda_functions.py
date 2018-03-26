def add_two(x, y):
    return x + y

# Anonymous functions - lambda

print((lambda x, y: x + y)(10, 5))

add = lambda x,y : x + y
print (add(10,5))

# First-class functions
# Una función puede ser argumento de otra funcion

def who(data, identify):
    return identify(data)

def my_identifier_function(some_data):
    return some_data['name']

user = {'name': 'jose', 'surname': 'Salvatierra'}

print (my_identifier_function(user))
print (who(user, my_identifier_function))

# Con función Lambda
print (who(user, lambda x: x['name']))







