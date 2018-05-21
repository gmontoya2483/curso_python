def starts_with_r(friend):
    return friend.startswith('R')


if __name__ == '__main__':
    friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
    start_with_r = filter(starts_with_r, friends)  # arg 1: function that returns True/False

    print(next(start_with_r))
    print(list(start_with_r))
    print(list(start_with_r))

    print('\n')

    # Usando lambda
    start_with_r_lambda = filter(lambda friend: friend.startswith('R'), friends)

    print(next(start_with_r_lambda))
    print(list(start_with_r_lambda))
    print(list(start_with_r_lambda))

    print('\n')

    # Utilizando Generator comprehension
    start_with_r_generator_comprehension = (friend for friend in friends if friend.startswith('R'))
    print(next(start_with_r_generator_comprehension))
    print(list(start_with_r_generator_comprehension))
    print(list(start_with_r_generator_comprehension))

