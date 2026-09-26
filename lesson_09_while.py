# task 1
count = 5
while count >= 1:
    print(count)
    count= count -1


#task2
end_number = int(input('kahan tuk numbers print krne hei'))
count = 1
while count<= end_number:
    print(count)
    count = count + 1


#task3
print('---PASSWORD PRACTICE---')
password = input('password likho:')
while password != 'python123':
    print('wrong password! password likho:')
    password = input('password likho:')
print('login successfull!')



#task4
print('---fitness check---')
fit_check = input('are you fit or not(yes/no):')
fit_check = fit_check.lower() 
while fit_check != 'yes':
    print('please try again')
    fit_check = input('are you fit or not(yes/no):')
    fit_check = fit_check.lower() 
print('thank you')


#task5
while True:
    answer = input('continue? (yes/no):').lower()
    if answer == 'no':
        print('program stopped')
        break
    print('continuing....')


#task6
user = input('kia ap apply krna chahogy?(yes/no):').lower()
while user == 'yes':
    print('ok lets start')
    user = input('kia ap apply krna chahogy?(yes/no):').lower()

print('tata...')


#task7
number = 1
total = 0
while number <=5:
    total = total + number
    number = number + 1
print(total)


#task8
for number in range(1,6):
    print(number)


#task9
total= 0
for number in range(1,6):
    total = total +number
print(total)


#task10
for number in range(1,4):
    print(number * 3)

#task11
for number in range(5):
    print('mei AI engineer ban rhi hon')
    print(number)


#task12
for number in range(1,11):
  if number == 5:
   continue
  print(number)


# task13
for number in range(1, 11):
    if number == 3 or number == 7:
        continue
    print(number)

#task14
total=0
for number in range(1,6):
  if number == 3:
   continue
  total=total+number
  print(total)