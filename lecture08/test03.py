class DTiSau :
    stu_name = ' '
    score = 0 
    gpa = 0 

    def hiStudent(self) :
        print(f'สวัสดี {self.stu_name}')

    def showScoreAndGrade(self) :
        print(f'คะแนน{self.score} ได้เกรด{self.gpa}')

obj01 = DTiSau()
obj02 = DTiSau()


obj01.stu_name = 'ไอก้อง'
obj01.hiStudent()
obj02.stu_name='ก้อง'
obj02.score = 99 
obj02.gpa=3.99