print('----AI IMAGE ACCESS CHECKER-----')
#Variables
user_credits = 15
credits_needed = 10
has_internet = True
has_api_key = False
has_free_trial = True
daily_images_generated = 5
daily_image_limit = 5
#Calculations
has_enough_credits = user_credits >= credits_needed
has_extra_credits = user_credits > credits_needed
needs_more_credits = user_credits < credits_needed
can_use_paid_api = has_internet and has_api_key
can_generate_with_trial = has_api_key or has_free_trial
within_daily_limit = daily_images_generated <= daily_image_limit
has_not_reached_limit = daily_images_generated != daily_image_limit
is_offline = not has_internet
cannot_use_paid_api = not(has_internet and has_api_key)

#Results
print(f'Has enough credits: {has_enough_credits}')
print(f'Has extra credits: {has_extra_credits}')
print(f'Needs more credits: {needs_more_credits}')
print(f'Can use paid api: {can_use_paid_api}')
print(f'Can generate with trial: {can_generate_with_trial}')
print(f'Within daily limit: {within_daily_limit}')
print(f'Has not reached limit: {has_not_reached_limit}')
print(f'Is offline: {is_offline}')
print(f'Cannot use paid api:{cannot_use_paid_api}')