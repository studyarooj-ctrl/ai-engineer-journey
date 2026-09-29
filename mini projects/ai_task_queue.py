print('====AI TASK QUEUE====')
tasks = ['write prompt','generate image','review result']
print(tasks)
item_removal = tasks.pop(0)
print(f'currently working on: {item_removal}')
print(f'bachi hoi task list:{tasks}')
print(f'pending tasks: {len(tasks)}')