# len() or indexing
print()
print('----len() or indexing-------')
ai_prompt= 'Create a robot teacher in lahore'

prompt_length= len(ai_prompt)
first_character=ai_prompt[0]
last_character= ai_prompt[-1]

print('---AI PROMPT INSPECTOR----')
print('Prompt:',ai_prompt)
print('Total characters:',prompt_length)
print('First character:',first_character)
print('Last character:',last_character)

print()
print('----STUDENT TASK----')
#Variables
chatbot_name= 'Lahore AI Helper'

#Calculations
total_characters= len(chatbot_name)
first_character= chatbot_name[0]
last_character= chatbot_name[-1]


#Result
print('Total characters:',total_characters)
print('First character:',first_character)
print('Last character:',last_character)
print()




# string methods strip(),upper(),lower()
print('----string methods strip(),upper(),lower()---------')
print()
print('---AI PROMPT CLEANER----')
#Variables
raw_prompt= '    Create A Futuristic Lahore Street At Night    '

#Calculations
clean_prompt= raw_prompt.strip()
lowercase_prompt= raw_prompt.lower()
uppercase_prompt= raw_prompt.upper()

#Result
print('Original raw prompt:', raw_prompt)
print('Clean prompt;',clean_prompt)
print('Lowercase prompt:',lowercase_prompt)
print('Uppercase prompt:',uppercase_prompt)

print()
print('----AI CHATBOT NAME FORMATTER-----')
 #Variables
raw_chatbot_name= '  Lahore Smart AI Assistant     '

#Original chatbot name
print('Original version:',raw_chatbot_name)

#Clean chatbot name
clean_name= raw_chatbot_name.strip()
print("Clean chatbot name:",clean_name)

#All-caps
uppercase_name= clean_name.upper()
print('All-caps chatbot name;',uppercase_name)

#All-small
lowercase_name= clean_name.lower()
print('All-small chatbot name;',lowercase_name)

#Length of chatbot name
length_chatbotname= len(clean_name)
print('Length of chatbot name;',length_chatbotname)



#concatination or f-string
print('----concatination or f-strings------')
print()
print('----AI ENGINEER PROFILE----')
#Variables
student_name= 'Study'
city='Lahore'
daily_study_hours= 2
#weekly study hours calculate kro
weekly_hours= daily_study_hours *7
#Concatination message
print("Hello, "+student_name+'! you are learning AI Engineering.')
#f-string message
print(f'{student_name} lives in {city} and studies {daily_study_hours} hours daily.')
print(f"{student_name}'s weekly study target is {weekly_hours} hours.")