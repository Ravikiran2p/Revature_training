terms = int(input("Enter a number: "))
sum = 0

for i in range(1, terms + 1):
    sum += i * i  # sum of squares

print(f"Sum is {sum}")
