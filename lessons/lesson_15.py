print('==== .pop use in list====')
print('.pop ke through hum through index list mei se items ko remove kr skty hei or unko kisi variable mei save kr skty hein or ye sub na tou .remove mei hei ')
print()
# lecture
# task1
ideas = ['chatbot','poster','voice app']
print(f'before removal list is {ideas}')
removed_idea = ideas.pop(1)
print(f'reoved item is {removed_idea}')
print(f' after removal list {ideas}')

print()
print('agr .pop() mein index number na ho tou woh last item hata deita hei')
last_item_removal = ideas.pop()
print(f'last item jo remove  howa hei index value na deine ki wajah se :{last_item_removal}')

# task2
list1 = ['draft','review','publish']
list2=list1.pop()
print(list2)
print(list1)


# task3
list3 = [10,20,30]
list4=list3.pop(0)
print(len(list3))
print(list4)

