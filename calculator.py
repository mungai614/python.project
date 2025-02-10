# first number
#operators 4
#second number

#number1 = float(input('Enter first number: '))
#op = input('Enter operator (+,-,*,/,^): ')
#number2 = float(input('Enter second number: '))
#print(number1,op,number2,)u

num_1 = int(input('Please, Enter the first number: '))
operator = input('Please, Enter the operator: ')
num_2 = int(input('Please, Enter the second number: '))
if operator == '+':
 print('Addition of {} + {} = '.format(num_1, num_2))
print(num_1 + num_2)
if operator == '_':
 print(' Subtraction of {} - {} = '.format(num_1, num_2))
print(num_1 - num_2)
if operator == '*':
  print('Multiplication of {} * {} = '.format(num_1, num_2))
print(num_1 * num_2)
if operator == '*':
 print('Division of {} / {} = '.format(num_1, num_2))
print(num_1 / num_2)



