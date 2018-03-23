# sets comprehension

friends = {'rolf', 'anna', 'charlie'}
guests = {'Jose', 'Rolf', 'ruth', 'Charlie', 'Michael'}

guests_lower = {name.lower() for name in guests}
present_friends = {str(name).capitalize() for name in guests_lower.intersection(friends)}
print(present_friends)


# Dictionary comprehension
names = ['Rolf', 'Anna', 'Charlie']
time_last_seen = [10, 15, 8]

friends_last_seen = {names[i]:time_last_seen[i] for i in range(len(names))}
print (friends_last_seen)

# usando zip()
print (zip(names, friends_last_seen)) # [('Rolf', 10), ('Anna', 15), ('Charlie', 8)]
friends_last_seen = dict(zip(names, time_last_seen))
print(friends_last_seen)



