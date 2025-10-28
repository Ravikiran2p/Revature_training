from interest_calculations import simple_interest
from shape_calulaton import circle_area,area_of_square,rectangle_area,

p=float(input("enter principle:"))
t=float(input("enter years:"))
r=float(input(" rata of interest:"))

print(f'simple_interest:{simple_interest(p=p,t=t,r=r)[0]}'
      f'amount:{simple_interest(p=p,t=t,r=r)[1]}')

print(f'circle_area:{circle_area(circle_area(10)[0]}')
f'area_of_square: {area_of_square(10)[1]}'}
