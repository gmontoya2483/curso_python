# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

if __name__ == '__main__':

    friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

    people = open('people.txt', 'r')
    people_nearby = [line.strip() for line in people.readlines()]  # [line1, line2, line3, etc]
    people.close()

    friends_nearby_list = [friend for friend in friends if friend.lower() in [person.lower() for person in people_nearby]]

    nearby_friends_file = open('nearby_friends.txt', 'w')

    for friend in friends_nearby_list:
        print(f'{ friend } is nearby! Meet up with them.')
        nearby_friends_file.write(f'{ friend }\n')

    nearby_friends_file.close()








