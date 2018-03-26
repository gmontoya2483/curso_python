"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movie
- See movies
- Find a movie
- Stop running the program

Tasks:
[X]: Decide where to store movies
[X]: What is the format of a movie
[X]: Show the user the main interface and get their input
[X]: Allow users to add a movie
[X]: Show all their movies
[X]: Find a movie
[X]: Stop running the program when they type 'q'
"""

movies = []


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command - Please try again.")

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    else:
        print("Stopping program...")


def add_movie():
    print('Adding a movie...')
    name = input("Enter the Name of the Movie: ")
    director = input("Enter the Director of the Movie: ")
    year = input("Enter the Year of the Movie: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies():
    print('Showing all movies...')
    for movie in movies:
        show_movie_detail(movie)
    print('')


def show_movie_detail(movie):
    print('')
    print(f'Name: { str(movie["name"]).capitalize() }')
    print(f'Director: { str(movie["director"]).capitalize() }')
    print(f'Year: { movie["year"] }')


def find_movie():

    find_by = (input('What property of the movie are you looking for? ')).lower()
    looking_for = input('Enter are you searching for? ')

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    for movie in found_movies:
        show_movie_detail(movie)
    print('')


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


if __name__ == '__main__':
    menu()
