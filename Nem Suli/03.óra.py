'''
name = input('Write your name: ')
age = input('Write your age: ')

age = int(age)
age = age + 1
print(f'Hello, {name}!')
print('Happy Birthday!')
print(f'You are {age} years old')
'''

# Exerice 1

length = input('Add meg a négyszög oldalhosszát: ')
width =  input('Add meg a négyszög oldalhosszát: ')

length = int(length)
width = int(width)

area = length * width

print(f'A négyszög területe: {area}')

# Exerice 2

item = input('What item would you like to buy? ')
price = float(input('What is the price: '))
quantity  = int(input('How many would you like to buy? '))

total =  price * quantity

print(f'You have bought {quantity} x {item}/s')
print(f'The total price is: {total}')
