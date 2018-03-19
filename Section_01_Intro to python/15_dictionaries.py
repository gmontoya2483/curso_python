my_friends = {
    'Jose': 6,
    'Rodolf': 12,
    'Anne': 6
}


my_friends = {
    'jose': {'last_seen':6},
    'Rolf': {'surname': 'Smith'},
    'Anne': 6
}


players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]

player_one = players[0]
print(player_one['name'])
print(player_one['numbers'])
print(sum(player_one['numbers']))