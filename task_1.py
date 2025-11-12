time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

parts = time_str.split(',')

total_minutes = 0

for part in parts:
    part = part.strip()

    elements = part.split()

    for elem in elements:     
        if 'h' in elem:
            hours = int(elem.replace('h', ''))
            total_minutes += hours * 60

        elif 'm' in elem:
            minutes = int(elem.replace('m', ''))
            total_minutes += minutes

        elif 's' in elem:
            seconds = int(elem.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes)