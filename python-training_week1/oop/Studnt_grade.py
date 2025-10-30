#from oop.Student_Details import StudentDetails
from oop.studextracurr import studextracurr
from oop.TeacherDetails import TeacherDetails

from oop.finaleval import finaleval
ccode=int(input('code:'))
cname=input('name:')


rollno=int(input('roll no:'))
sname=input('name:')
m1=int(input('m1:'))
m2=int(input('m2:'))
m3=int(input('m3:'))
exam1=int(input('exam1:'))
exam2=int(input('exam2:'))


'''stud=studextracurr(ccode,cname,rollno,sname,m1,m2,m3,exam1,exam2)
print(f'{stud.get_rollno}\n {stud.sname}\n'
      f'{stud.calc_total()}\n'
      f'{stud.calc_avg()}')
print(f'{stud.calc_extracurr()}')
'''

empid=int(input('empid:'))
tname=input('tname:')
dept=input('dept:')

"""Teacher=TeacherDetails(ccode,cname,dept,tname,empid)
Teacher.Display()"""

feedbackfromTeacher=input('Enter feedback:')
finaleval=finaleval(ccode,cname,rollno,sname,m1,m2,m3,exam1,exam2,empid,tname,dept,feedbackfromTeacher)

print(f'{finalevel.get_rollno} \n{finaleval.sname}\n')
print(f'{finaleval.display()}\n'
      f'{finaleval.display()[0]}\t {finaleval.display()[1]}\n'
      f'{finaleval.calc_total()[2]}\n'
      f'{finaleval.calc_avg()}\n'
      f'{finaleval.calc_extot()}\n' )
finaleval.Teacher_ddisplay()
print(f'{finalevel.feedbackfromTeacher}')
