#Variables
total_credits=250
credits_per_image=12
price_per_image=35
monthly_tool_cost=500

print('----AI IMAGE GENERATION BUDGET CALCULATOR-----')
print()
#calculations
#woh kitni images generate kr skta hei total credits se
complete_images=total_credits // credits_per_image
print('Complete images:',complete_images)

#kitne credits bachay
remaining_credits= total_credits % credits_per_image
print('Remaining credits:',remaining_credits)

#poray month ka revenue
monthly_revenue= complete_images * price_per_image
print('Monthly revenue;',monthly_revenue)

#Estimated monthly profit kitna hei
estimated_profit= monthly_revenue - monthly_tool_cost
print('Monthly profit;',estimated_profit)

#daily ka profit kitna hei
daily_profit= estimated_profit / 30
print('Daily profit;', daily_profit)

#Credits squared
credits_squared= total_credits ** 2
print('Credits ka square:', credits_squared)

#5PKR discount per image
discounted_revenue= (price_per_image - 5) * complete_images
print('Discounted revenue;',discounted_revenue,'PKR')