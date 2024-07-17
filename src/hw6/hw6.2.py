mean = int(input('Введіть число більше або дорівнює 0 і менше ніж 8640000: '))

if 0 <= mean < 8640000:
    days = mean // 86400
    hours = mean // 3600 - days * 24
    minutes = mean // 60 - days * 1440 - hours * 60
    seconds = mean - days * 86400 - hours * 3600 - minutes * 60


    if days > 14:
        variant = days % 10
    else:
        variant = days

    days_mapping = {
     "1": [2, 3, 4],
     "2": [1]
    }

    wrd = 'днів'
    if variant in days_mapping['1']:
        wrd = 'дні'
    elif variant in days_mapping['2']:
        wrd = 'день'

    print(f'{days} {wrd}, {hours:02}:{minutes:02}:{seconds:02}')
else:
    print('Try again!')