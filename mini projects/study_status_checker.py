study_time = int(input('kitna time study kia aj tumne:'))

if study_time >= 120:
    print('Excellent study day!')
elif study_time >= 60:
    print('good progress')
elif study_time >= 1:
    print('keep going')
else:
    print('aj study start karo')