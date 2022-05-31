i = 1
print(id(i))
print(type(i))

name = input('Enter pet name: ')
print('Your pet name is', name)

age = input('How many pet years old? ')
age = int(age)
print(type(age))


# Exercise 1
weight = input('Input pet weight: ')
print(f'Your pet is {name}, {age} years old and weight: {weight}')

# Exercise 2
lucky_num = input('Input your lucky number: ')
print('you inputed {x} as your lucky number'.format(x=lucky_num))
