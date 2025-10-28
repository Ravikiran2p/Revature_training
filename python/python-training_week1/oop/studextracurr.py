from Student_Details import StudentDetails

class studextracurr(StudentDetails):
    def __init__(self,ccode,cname,rollno,sname,m1,m2,m3,exam1,exam2):
        super().__init__(ccode,cname,rollno,sname,m1,m2,m3)
        self.exam1=exam1
        self.exam2=exam2

    def calc_extracurr(self):
        return self.exam1+self.exam2

