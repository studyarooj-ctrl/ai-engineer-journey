print('welcome in your earning calculator')
name = input('enter your name please:')
print('ok',name,'give me your client name')
client_name = input('client name please:')
project_fee = int(input('fee per project:'))
projects_quantity= int(input('es month kitny projects kiye:'))
ai_tools_cost = int(input('ai tools pr monthly cost kitni hei:'))
print()
totalincome=project_fee * projects_quantity
print('so total income in a month is :', totalincome)
net_income = totalincome-ai_tools_cost
print('after deduction of ai tools cost your total earning is :',net_income)
print()
print('----teacher improve code---')
print('Welcome to your AI Freelance Earnings Calculator!')

freelancer_name = input('Enter your name please: ')
client_name = input('Enter your client name please: ')

project_fee = float(input('Fee per project in PKR: '))
total_projects = int(input('Is month kitne projects kiye: '))
ai_tools_cost = float(input('AI tools ki monthly cost in PKR: '))

total_income = project_fee * total_projects
net_income = total_income - ai_tools_cost

print()
print('--- AI FREELANCE EARNINGS REPORT ---')
print('Freelancer:', freelancer_name)
print('Client:', client_name)
print('Project fee:', project_fee, 'PKR')
print('Projects completed:', total_projects)
print('Total income:', total_income, 'PKR')
print('AI tools cost:', ai_tools_cost, 'PKR')
print('Net earning:', net_income, 'PKR')
print('Keep building AI skills,', freelancer_name + '!')