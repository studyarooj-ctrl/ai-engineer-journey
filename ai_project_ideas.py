print('---AI PROJECT IDEA LIST PROGRAM---')
ideas = ['study bot','image maker','voice helper']
print(ideas)
new_idea = input('new idea to add please:')
ideas.append(new_idea)
print(ideas)
print(len(ideas))
first_idea = ideas[0]
last_idea = ideas[-1]
print(f'First idea is {first_idea} and last idea is {last_idea}.')