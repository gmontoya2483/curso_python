import datetime



# time
t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print('\n')

# date time
dt = datetime.datetime(2017, 5, 23, 13, 26, 40, 100000)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)

print(dt.weekday())
print(dt.isoweekday())
print(dt.isocalendar())

print(dt.time())
print(dt.date())
print('\n')

# date time constructors
dt_fix_date = datetime.datetime(2017, 5, 23, 13, 26, 40, 100000)

dt_today = datetime.datetime.today()  # Return the current local time without considering the time zone
dt_now = datetime.datetime.now()  # Nos da la opcion de pasarle el time zone.
dt_utcnow = datetime.datetime.utcnow()

print(f'fixed date: { dt_fix_date }')
print(f'date today: { dt_today }')
print(f'date now: { dt_now }')
print(f'date utcnow: { dt_utcnow }')
