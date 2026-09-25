#Esme hum if,else or elif conditions ko samjhein ge
study_hours= 3
daily_goal = 2

print('---STUDY GOAL CHECKER----')

if study_hours >= daily_goal:
    print('Great work! You completed your daily AI study goal.')

print('Keep learning Python!')

print()
print('----AI API CREDIT MESSAGE----')

#Variables
api_credits = 8
credits_needed = 5

if api_credits >= credits_needed:
    print('You have enough credits to use the  AI API.')

print('AI API credit check completed.')

print()
print('---AI IMAGE CREDIT CHECKER----')

user_credits = 7
credits_needed = 10 

if user_credits >= credits_needed:
    print('You can generate an AI image.')
else:
    print('Not enough credits. Please add more credits.')

print()
print('----STUDENT TASK-----')
print('---AI STUDY GOAL RESULT---')
# Variables
study_hours = 1
daily_goal = 2

# study hours goal se equal ya greater check krne ke liye >= hoga
if study_hours >= daily_goal:
    print('Great! You completed your AI study goal.')
else:
    print('Keep going! Study more to complete your AI goal.')

#elif practice
age = 15

if age>=18:
    print('You can vote')
elif age >=13:
    print('You are a teenager')
else:
    print('You are a child')