def get_user_profile(user):
    from users.models import Profile
    profile = Profile.objects.get(user=user)
    return profile

def format_name(user, format):
    profile = get_user_profile(user)

    first = profile.first_name.title()
    middle = profile.middle_name.title()
    middle_initial = False
    if middle:
        middle_initial = profile.middle_name[0].title()
    last = profile.last_name.title()

    if format == 'full name':
        name = f'{first} {middle} {last}'
    elif format == 'last, first':
        name = f'{last}, {first} {middle}'
    elif format == 'last, first MI':
        if middle_initial:
            name = f'{last}, {first} {middle_initial}.'
        else:
            name = f'{last}, {first}'
    elif format == 'path':
        name = f'{last}_{first}_{middle}'
    return name

def format_currency(number):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    amount = locale.currency(number, grouping=True)
    
    if amount[-2] is '0':
        if amount[-1] is '0':
            amount = amount[:-1]
            amount = amount[:-1]
            amount = amount[:-1]
    return amount

def format_date(date, format):
    from .data import Calendar
    months = Calendar.months
    
    if format == 'MMM-DD':

        month = months[date.month][0]
        day = date.day
        if day < 10:
            day = f'0{day}'
        date = f'{month.upper()}-{day}'
    
    return date

def format_time(time, format):
    hour = time.hour
    minutes = time.minute
    if format == 'HH:MM':
        if hour < 10:
            hour = f'0{hour}'
        if minutes < 10:
            minutes = f'0{minutes}'
        time = f'{hour}:{minutes}'
    
    return time

def get_extension(filename):
    extension = ''
    found = False
    for char in filename:
        if char is '.':
            found = True
        if found:
            extension += char
    return extension.lower()

def get_profile_picture_upload_path(instance, filename):
    user_name = format_name(instance.user, format='path')
    extension = get_extension(filename)

    path = f'users/{user_name.lower()}/images/profile_picture{extension}'

    return path

def get_document_upload_path(instance, filename):
    user_name = format_name(instance.user, format='path')
    extension = get_extension(filename)

    path = f'{instance.name.lower()}s/{instance.file_date}{extension}'

    return f'users/{user_name.lower()}/documents/{path}'
