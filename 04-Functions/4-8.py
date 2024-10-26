def time_string(hours, minutes, time_format):

    if time_format == "24":
        return f'{hours:02}:{minutes:02}'

    if time_format == '12':
        if hours == 0:
            formatted_time = f'12:{minutes:02}am'
        elif hours == 12:
            formatted_time = f'12:{minutes:02}pm'
        elif hours > 12: 
            formatted_time = f'{hours - 12}:{minutes:02}pm'
        else:
            formatted_time = f'{hours}:{minutes:02}am'

        return formatted_time

entered_hours = int(input('Hours: ')) 
entered_minutes = int(input('Minutes: '))
entered_format = (input('Format: '))

print(f'The time is: {time_string(entered_hours, entered_minutes, entered_format)}')