first_name = input('Please enter your name: ')
last_name = input('Please enter your surnmae: ')
age = input('Please enter your age: ')
day_of_birthday = input('Please enter your birth year: ')
user_information = []
user_information.append(first_name)
user_information.append(last_name)
user_information.append(age)
user_information.append(day_of_birthday)
for i in user_information:
    print(i)
if int(age) < 18:
    print("You can't go out because it's to dangerous")
else:
    print('You can go out to the street.')
