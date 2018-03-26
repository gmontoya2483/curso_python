def i_return():
    return 5 + 5

def i_print():
    addition = 5 + 5
    print (addition)
    return addition


result = i_return()
another = i_print()

print(f'Result is {result}')
print(f'Another is {another}')