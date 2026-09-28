#Conditional operators
print('----Conditional operators------')
print('----AI Credit Checker-----')
api_credits= 15
credits_needed= 10

has_enough_credits = api_credits >= credits_needed
has_exact_credits = api_credits == credits_needed
has_more_credits = api_credits > credits_needed
has_zero_credits = api_credits == 0
print(f'Has enough credits: {has_enough_credits}')
print(f'Has exact credits: {has_exact_credits}')
print(f'Has more credits: {has_more_credits}')
print(f'Has zero credits: {has_zero_credits}')

print()
print('----Student Task----')
print('-----AI ENGINEER STUDY CHECKER--------')
print()
#Variables
study_hours = 2
daily_goal = 3


#Comparisons
goal_completed = study_hours >= daily_goal
needs_more_study = study_hours < daily_goal
studied_exact_goal = study_hours == daily_goal
studied_zero_hours = study_hours == 0
has_studied = study_hours > 0

#Results
print(f'Kia study hours goal se ziada ya equal hein: {goal_completed}')
print(f'kia study hours goal se less hein: {needs_more_study}')
print(f'kia study hours goal se same hein: {studied_exact_goal}')
print(f'kia study hours zero ke equal hein: {studied_zero_hours}')
print(f'kia study hours zero se greater hein: {has_studied}')



#logical operators
print()
print('----logical operators-----')
print()
print('-----AI TOOL ACCESS CHECKER-----')

has_internet = True
has_api_key = True
daily_requests = 8
request_limit = 10

can_use_ai_tool = has_internet and has_api_key
within_request_limit = daily_requests <= request_limit
needs_more_request = daily_requests != request_limit
is_offline = not(has_internet)

print('Can use AI tool:', can_use_ai_tool)
print('Within request limit:',within_request_limit)
print('Requests are not exactly at limit;',needs_more_request)
print('Is offline;', is_offline)

print()
print('----AI COURSE ACCESS CHECKER-----')
#Variables
has_account = True
has_completed_payment = False
has_free_trial = True
videos_watched = 5
videos_limit = 5
#Calculations
has_full_access = has_account and has_completed_payment
can_watch_course = has_completed_payment or has_free_trial
within_video_limit = videos_watched <= videos_limit
has_not_reached_limit = videos_watched != videos_limit
has_no_account = not(has_account)
#Results
print('Full access:',has_full_access)
print('Can watch course',can_watch_course)
print('Within video limit:',within_video_limit)
print('Has not reached video:',has_not_reached_limit)
print('Has no account;',has_no_account)