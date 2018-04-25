import datetime

d = datetime.date(2016, 7, 24)
print(d)
print('\n')

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.month)
print(tday.weekday())  # (Monday 0  Sunday 6)
print(tday.isoweekday())  # (Monday 1  Sunday 7)
print('\n')


# Time deltas
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(f'Today: { tday }')
print(f'+ 7 days: { tday + tdelta }')
print(f'- 7 days: { tday - tdelta }')
print('\n')

# Calculando el delta
bday = datetime.date(2019, 1, 9)
tday = datetime.date.today()
till_bday = bday - tday

print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())
