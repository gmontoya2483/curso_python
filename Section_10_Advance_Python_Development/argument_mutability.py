friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}


def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))
print(friends_last_seen)

print('\n')

see_friend(friends_last_seen, 'Rolf')
print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))
print(friends_last_seen)

print('\n')



def increase_age(current_age):
    print(id(current_age))
    current_age = current_age + 1
    print(current_age)

age = 20

print(id(age))
print(age)

print('\n')

increase_age(age)
print(id(age))
print(age)


