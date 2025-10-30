from studextracurr import studextracurr
from TeacherDetails import TeacherDetails


class finaleval(studextracurr, TeacherDetails):
    def __init__(self,ccode,cname,rollno,sname,m1,m2,m3,exam1,exam2,empid,tname,dept,feedbackfromTecaher):
        super().__init__(ccode,cname,empid,tname,dept)
        self.feedbackfromTeacher=feedbackfromTecaher