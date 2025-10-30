from oop.ArithCalculations import ArithCalculations
from oop.AgeNotEnoughError import AgeNotEnoughError

n1 = int(input('Enter your first number: '))
n2 = int(input('Enter your second number: '))
age = int(input('Enter your age: '))

calc = ArithCalculations(n1, n2)

print(f'Addition: {calc.add()}')
print(f'Subtraction: {calc.sub()}')
print(f'Multiplication: {calc.mul()}')

try:
    if n2 == 0:
        raise ZeroDivisionError('Denominator cannot be zero.')
    if age < 18:
        raise AgeNotEnoughError('You are a minor.')
except ZeroDivisionError as zde:
    print(f'Error: {zde}')
except AgeNotEnoughError as ae:
    print(f'Error: {ae}')

try:
    l1 = [1, 5, 7, 3]
    val = l1[1]
    res = calc.div()
except ZeroDivisionError as zde:
    print(f'Error: {zde} - Denominator issue')
except IndexError as ie:
    print(f'Error: {ie} - Index not found')
except Exception as ex:
    print('Something went wrong:', ex)
else:
    print(f'Division Result: {res}')
    print(f'List Value: {val}')
finally:
    print("Done >>!!")
