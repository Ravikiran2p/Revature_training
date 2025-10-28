"""banking interest calculations"""
from interest_calculations import simple_interest,compound_interest
p=float(input("enter principal amount: "))
t=float(input("enter number of years: "))
r=float(input("enter real interest rate: "))

si,amount=simple_interest(p=p,t=t,r=r)
print(f"The amount is: {amount}")
