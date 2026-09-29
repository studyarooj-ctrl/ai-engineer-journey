print('===AI IDEAS REMOVE PRACTICE===')
ideas = ['chatbot','image maker','voice helper']
print(f'before removal:{ideas}')
remove_idea = input('which idea you want to remove?')
ideas.remove(remove_idea)
print(f'after updation: {ideas}')
print(len(ideas))