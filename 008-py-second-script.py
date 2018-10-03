# learn about python data types
# learn about strings
# some more advanced string operations

class student:
    def __init__(self, id, fname, lname, school):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.school = school
    def process_students_data(self, element):
        id, fname, lname, school = element.split(",")
        return [{
            'id': id,
            'fname':fname,
            'lname': lname,
            'school': school
        }]

def process_student_lines(element):
        id, fname, lname, school = element.split(",")
        return [{
            'id': id,
            'fname':fname,
            'lname': lname,
            'school': school
        }]

#studentobj = 
#studentline= "10,Vishal,Khondre,test"
#studentdata = process_student_lines(studentline)
#print(studentdata)

with open("C:\code\learnPython\studentsdata.csv") as f:
    data = f.readlines()
for studentline in data:
    print(studentline)
    studentdata = process_student_lines(studentline)
    print(studentdata)
    print('\n')
    studentdata
