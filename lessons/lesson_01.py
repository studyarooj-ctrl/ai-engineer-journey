print('-----print function seekha -----')
print()
print("salam everyone")
print("my name is arooj")
print('mei ne course start kia hei ai engineering ke name se')
print('or aj seekha ke print command kia hein or double walay strings hotay hei or single quotes walay bhi')
print("This is a string using double quotes.")
print('This is a string using single quotes.')
print('or abhi test kr rhi hon command ko')
print("Python is my first programming language.")
print('I can use single quotes too.')
print("My goal is to become an AI Engineer.")
print('thankyou')

# print function
print('hello,python!')
print(100)
print(10.5)
# output
# hello,python!
# 100
# 10.5

# multiple values or parameters
#sep separator
print('15',"08","2026",sep="=")  # with strings
print(12,50,56,sep="-")  #with integers
print(12.8,78.0,4.6,sep=",")  # with float decimal numbers
#output
# 15=08=2026
# 12-50-56
# 12.8,78.0,4.6

#end character
print('python is ',end="  ")
print('awesome!')   # output: python is awesome!
print('python is ',end="u")
print('awesome!')  # output: python is uawesome!

#escape sequences
print('my name is areena\n or i live in lahore.\t or sunao kia ho raha hei')
print('name:\trahul\nrole:\tpython developer')
#output:  name:   rahul
#         role:   python developer

#f-string 
name = 'sara'
age = 22
print(f'mera naam {name} hai aur meri umar {age} saal hai.')
#output: mera naam ali hai aur meri umar 22 saal hai.

#variable or id() function
x=10
name= 'ali'
print(id(name))
# output :2243662990624 her variable ki alag memory location hoti hei


# type casting
x ='25'
x_num = int(x)
price = 100
price_float = float(price)
print(type(x))  #output: class:str
print(type(x_num))  # output: class:int
print(type(price))  # output:class:int
print(type(price_float))  #output: class:float

# input() function user se input leine ke liye or hamesaha string format hi hota hei by default
name= input('Enter your name:')
print(f'Welcome {name}!')

#practice task
first_name = input('Enter your name:')
math_marks = int(input('Enter your math marks:'))
physics_marks= int(input('Enter your physics marks:'))
total_marks = math_marks + physics_marks
print(f'hello {first_name}!, your math marks is {math_marks} out of 100 or physics marks is {physics_marks} out of 100 so total number is {total_marks}')


#practice set 
x=2
x='too far'
print(id(x))

age = int(input('Enter your age:'))
next_age = age + 1
print(f'Next year age is: {next_age}')

user_city = input('Enter your city name:')
user_age = int(input('Enter your age:'))
print(f'Aap {user_city} mei rehte hein aur apki age {user_age} saal hai.')
print('Aap '+ user_city+' mei rehte hein aur apki age '+ str(user_age) + ' saal hei')  #concatination style

y= '20'
z = '40'
f = y + z
print(f)  # humne seekha jub do string ko plus krte hein tou concatination hota hei 

#Concatenation ke rules (str + str vs str + int)
#                           true        error