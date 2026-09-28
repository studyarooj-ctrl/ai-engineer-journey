age = int(input('Your age please:'))
ticket_status = input('kia apne ticket li hei yes or no:')
banned_status = input('apka banned status kia hei:')
ticket = ticket_status.lower() == 'yes'
banned = banned_status.lower() == 'yes'

if banned:
    print('Entry denied: You are banned')
elif age < 18:
    print('Entry denied: You must be at least 18')
elif not ticket:
    print('Entry denied:Valid ticket required')
else:
    print('Entry allowed:welcome')