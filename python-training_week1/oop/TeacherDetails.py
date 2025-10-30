from oop.college import College

class TeacherDetails(College):
    def __init__(self,ccode,cname,empid,tname,dept):
        StudentDetail__init__(ccode.cname)
        self.empid=empid
        self.tname=tname
        self.dept=dept

    def Teacher_display(self):
        print(f'{super()._ccode} \t {super()._cname}\n'
              f'{self.empid} \n {self.tname} \n {self.dept}')