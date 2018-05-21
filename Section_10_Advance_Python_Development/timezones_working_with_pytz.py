import datetime
import pytz

# Crear un datetime tz aware
dt_fix_date_aware = datetime.datetime(206, 7, 27,12, 30,45, tzinfo=pytz.UTC)
print(f'Fixed date tz aware UTC: { dt_fix_date_aware }')

# usar el now, con el parametro del tz
dt_now_aware = datetime.datetime.now(tz=pytz.UTC)
print(f'Now date tz aware UTC: { dt_now_aware }')

# usar el now, con el parametro del tz
vienna_tz = pytz.timezone('Europe/Vienna')
dt_vienna_now_aware = datetime.datetime.now(tz=vienna_tz)
print(f'Now date in Vienna aware: { dt_vienna_now_aware }')


# usar el utcnow(), y aplicarle el tz
dt_utcnow_aware = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(f'utcnow tz aware replace(UTC): { dt_utcnow_aware }')

print('\n')


# Convertir a diferentes time zones
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
dt_vienna = dt_utcnow.astimezone(pytz.timezone('Europe/Vienna'))
dt_bs_as = dt_utcnow.astimezone(pytz.timezone('America/Argentina/Buenos_Aires'))

print(f'UTC : { dt_utcnow }')
print(f'US/Mountain : { dt_mtn }')
print(f'Europe/Vienna : { dt_vienna }')
print(f'America/Argentina/Buenos_Aires : { dt_bs_as }')

print('\n')


# Convertir un datetime Naive a Aware
dt_vienna_naive = datetime.datetime.now()
vienna_tz = pytz.timezone('Europe/Vienna')
dt_vienna_aware = vienna_tz.localize(dt_vienna_naive)
dt_utc_aware = dt_vienna_aware.astimezone(pytz.timezone('UTC'))

print(f'Local datetime (naive) : { dt_vienna_naive }')
print(f'Europe/Vienna (aware) : { dt_vienna_aware }')
print(f'utc (aware) : { dt_utc_aware }')

print('\n')

# Formating dates
dt = dt_utcnow.astimezone(pytz.timezone('Europe/Vienna'))
print(f'ISO Format : { dt.isoformat() }')
print(f"'%B %d, %Y': { dt.strftime('%B %d, %Y')}")

print('\n')

# Convertir un string a un datetime
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(f'Date from String: { dt }')


# Avriguar todos los timezones
for tz in pytz.all_timezones:
    print(tz)


