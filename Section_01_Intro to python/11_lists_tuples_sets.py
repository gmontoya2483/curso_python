"""
Data structures,
collection,
iterables,
sequences,
etc
List, touples and set
""" 

# List
my_list_variable = ['hello', 'hi', 'nice to meet you']
print(my_list_variable)
print (my_list_variable[0])
my_list_variable.append('another string')
print(my_list_variable) 

# Tuple
my_tuple_variable = ('hello', 'hi', 'nice to meet you')
print(my_tuple_variable)
print (my_tuple_variable[0])

my_short_tuple_variable = ('hello',)
print(my_short_tuple_variable)

my_tuple_variable = my_tuple_variable + ('another string',)
print (my_tuple_variable)

# Sets
my_set_variable = {'hello', 'hi', 'nice to meet you'}
print(my_set_variable)
my_set_variable.add('another string')
print(my_set_variable)

my_set_variable.add('hello')
print(my_set_variable)

