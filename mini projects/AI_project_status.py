print('=== ai project status ===')

statuses = ['planned', 'in progress', 'planned']
print(statuses)
replace_status = int(input('kis project ka status badalna hei(1-3)?'))
index = replace_status -1
new_status = input('kis se replace krna hei')
statuses[index]= new_status
print(statuses)
for status in statuses:
    print(status)
