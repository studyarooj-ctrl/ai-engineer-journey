print('---STUDENT GRADE CHECKER----')
marks = int(input("Apne marks batao:"))

if marks >= 80:
    print('Your grade is A')
elif marks >= 70:
    print('Your grade is B')
elif marks >= 60:
    print('Your grade is C')
elif marks >= 50:
    print('Your grade is D')
else:
    print('Fail')