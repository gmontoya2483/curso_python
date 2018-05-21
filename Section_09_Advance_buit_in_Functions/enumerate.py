top_friends = ['Jose', 'Rolf', 'Anna','Santiago']

for i, friend in enumerate(top_friends):
    print(f'My top { i+1 } friend is { friend }.')

print('\n')

friends_generator = enumerate(top_friends)

print(next(friends_generator))
print(list(friends_generator))
print(list(friends_generator))
