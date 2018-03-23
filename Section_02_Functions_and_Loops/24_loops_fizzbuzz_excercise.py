for num in range(1, 101):
    to_show = ''
    if (num % 3) == 0:
        to_show += 'Fizz'
        
    if (num % 5) == 0:
        to_show += 'Buzz'
    
    if to_show == '':
        print (num)
        continue

    print (to_show)

