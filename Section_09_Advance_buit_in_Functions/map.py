def to_lower(friend):
    return friend.lower()


if __name__ == '__main__':
    friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

    # Using a regular function
    friends_lower_map_regular = map(to_lower, friends)

    print(next(friends_lower_map_regular))
    print(list(friends_lower_map_regular))
    print(list(friends_lower_map_regular))

    print('\n')

    # Using map() con lambda
    friends_lower_map_lambda = map(lambda x: x.lower(), friends)

    print(next(friends_lower_map_lambda))
    print(list(friends_lower_map_lambda))
    print(list(friends_lower_map_lambda))

    print('\n')

    # Using generator comprehension
    friends_lower_generator_comprehension = (friend.lower() for friend in friends)

    print(next(friends_lower_generator_comprehension))
    print(list(friends_lower_generator_comprehension))
    print(list(friends_lower_generator_comprehension))

