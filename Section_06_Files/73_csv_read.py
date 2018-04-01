file = open('csv_data.txt', 'r')
lines = [line.strip() for line in file.readlines()]  # [line1, line2, line3, etc]
file.close()

lines = lines[1:]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].capitalize()
    degree = person_data[3].title()

    print(f'{ name } is { age }, studying { degree } at { university }')

# Como crear un row
sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)


