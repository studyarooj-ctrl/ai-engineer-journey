print('-----AI PROMPT FORMATTER-----')
print()
#Variables banao
raw_prompt= '   Create A Cinematic AI Scene In Lahore At Night  '

print(f'Original Raw  prompt: {raw_prompt}.')
#Clean prompt version
clean_prompt= raw_prompt.strip()
print(f'Clean version of prompt : {clean_prompt}')
#Lowercase prompt version
lowercase=clean_prompt.lower()
print(f"Prompt version  in lowercase:{lowercase}")
#Uppercase prompt version
uppercase= clean_prompt.upper()
print(f'Prompt version in uppercase:{uppercase}')
#Length of the clean prompt
total_characters= len(clean_prompt)
print(f'the total characters length of prompt is {total_characters}.')
#First character of prompt
first_character= clean_prompt[0]
print(f'First character of prompt is {first_character}.')
#Last character of the prompt
last_character= clean_prompt[-1]
print(f'The last character of the prompt is {last_character}.')
#Concatination message
print('Your cleaned AI prompt is: '+clean_prompt)
#f-string message
print(f'Prompt contains {total_characters} characters and start with "{first_character}".')