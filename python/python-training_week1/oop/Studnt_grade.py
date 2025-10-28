from oop.Student_Details import StudentDetails
from oop.studextracurr import studextracurr

ccode=int(input('code:'))
cname=input('name:')


rollno=int(input('roll no:'))
sname=input('name:')
m1=int(input('m1:'))
m2=int(input('m2:'))
m3=int(input('m3:'))
exam1=int(input('exam1:'))
exam2=int(input('exam2:'))


stud=studextracurr(ccode,cname,rollno,sname,m1,m2,m3,exam1,exam2)
print(f'{stud.get_rollno}\n {stud.sname}\n'
      f'{stud.calc_total()}\n'
      f'{stud.calc_avg()}')
print(f'{stud.calc_extracurr()}')