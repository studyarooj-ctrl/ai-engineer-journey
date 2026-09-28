#Arithmetic operators
print('----arithmetic operators-----')
study_hours_today = 2
study_hours_yesterday = 4

total_study_hours = study_hours_today+study_hours_yesterday
difference_hours= study_hours_today-study_hours_yesterday
weekly_study_hours= study_hours_today*7
Average_hours= total_study_hours/2

print('TOTAL STUDY HOURS:',total_study_hours)
print('Difference in hours:',difference_hours)
print('Weekly study hours:',weekly_study_hours)
print('Average study hours:',Average_hours)


print()
print('----AI PROJECT COST CALCULATOR----')

project_price= 10000
ai_tools_cost= 2500
internet_cost= 1500

total_cost=ai_tools_cost+internet_cost
profit=project_price-total_cost
monthly_profit=profit*4
daily_profit=monthly_profit/30

print('TOTAL COST:',total_cost)
print('PROFIT FROM ONE PROJECT:',profit)
print('ESTIMATED MONTHLY PROFIT:',monthly_profit)
print('AVERAGE PROFIT PER DAY:',daily_profit)

print()
print('----AI API CREDITS CALCULATOR----')
#variables
api_credits=103
credits_per_request=8


#calculation
total_requests=api_credits//credits_per_request
remaining_credits=api_credits%credits_per_request
double_credits=api_credits**2
calculation_one=10+2*3
calculation_two=(10+2)*3

#output
print('TOTAL REQUESTS:',total_requests)
print('REMAINING CREDITS:',remaining_credits)
print('Credits squared:',double_credits)
print('Without Parenthesis:',calculation_one)
print('With Parenthesis:',calculation_two)