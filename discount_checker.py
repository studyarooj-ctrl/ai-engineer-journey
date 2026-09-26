print('---DISCOUNT CHECKER---')
total_bill = int(input('total bill:'))
is_member = input('are you member (yes/no):')
is_member =is_member.lower() == 'yes'
if total_bill >= 5000 and is_member:
    print('You got 20% discount')
elif total_bill >= 5000 or is_member:
    print('You got 10% discount')
else:
    print('sorry! no discount')