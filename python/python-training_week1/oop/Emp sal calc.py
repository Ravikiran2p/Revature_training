from oop.Employee import Employee

empid=int(input('enter employee id:'))
empname=input('enter employee name:')
bp=float(input('enter employee bp:'))

employee = Employee(empid,empname,bp)

print(f'empid:{employee.empid},empname:{employee.empname}\n'
      f'grosspay:{employee.calc_grosspay()}\n'
      f'net pay:{employee.netpay()}')
