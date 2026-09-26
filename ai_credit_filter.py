print('---AI CREDIT FILTER---')
#Variables
credit_needed =3
total_credits = 0
for number in range(1,11):
    if number == 4 or number ==8:
        continue
    print(f'her image ke liye uska number: {number}')
    total_credits =  total_credits + credit_needed
print(total_credits)
