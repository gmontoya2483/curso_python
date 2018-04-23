from datetime import datetime, timezone, timedelta

# Naive object
ahora_naive = datetime.now() # Current local time
print(ahora_naive)


# aware object
ahora_aware = datetime.now(timezone.utc)
print(ahora_aware)
print('\n')


# time dela
today = datetime.now(timezone.utc)
print(f' Ahora: { today }')

later = today + timedelta(hours=3)
print(f' Mas tarde: { later }')

tomorrow = today + timedelta(days=1)
print(f' Manana: { tomorrow }')

yesterday = today + timedelta(days=-1)
print(f' Ayer: { yesterday }')

print('\n')


# date format strftime() and strptime()

today = datetime.now(timezone.utc)
print(f"Ahora Formatted: { today.strftime('%d-%m-%Y %H:%M') }")  # string format time

user_date = input('Enter the date in YYYY-mm_dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time
print(user_date)

print('\n')