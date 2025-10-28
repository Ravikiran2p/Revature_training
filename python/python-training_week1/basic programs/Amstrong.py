'''
25/10/2025
'''
# 25/10/2025

numstr = input('Enter a number: ')
numlen = len(numstr)
num = int(numstr)

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** numlen  # raise each digit to the power of numlen
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


