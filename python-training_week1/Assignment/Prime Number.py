start= int(input("Enter a Start number: "))
end=int(input("Enter a End number: "))
print(f"prime numbers between {start} and {end}:")
for num in range(start,end+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num % i==0:
                break
        else:
            print(num,end=" ")