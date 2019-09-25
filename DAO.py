import Models
import csv

class StudentDAO:
    student_list=[]
#Reading student CSV file and getting the student list    
    def __init__(self):
            with open('students.csv',mode='r+',encoding='utf8')as f:
                for line in f.read().split('\n'):
                    self.email, self.s_name, self.s_password = line.split(',')
                    student=Models.Student(self.email,self.s_name,self.s_password)
                    StudentDAO.student_list.append(student)        

    def get_students(self):
                return StudentDAO.student_list
            
# Validating the student email and password
    def validate_user(self, email, pw):
        self.get_students()
        for student in StudentDAO.student_list:
            if student.get_email()==email:
                if  pw==student.get_password():
                    return True
                else:
                    return False

#Getting the details of a student by email
    def get_student_by_email(self, email):
        for student in StudentDAO.student_list:
            if student.get_email()==email:
                return(student)

class CourseDAO:
#Reading the courses file and getting the list of all courses
    def __init__(self):
        self.course_list=[]
        with open('courses.csv',mode='r+',encoding='utf8')as f:
                for line in f.read().split('\n'):
                    self.c_id, self.c_name, self.instructor = line.split(',')
                    course =Models.Course(self.c_id, self.c_name, self.instructor)                    
                    self.course_list.append(course)
        
    def get_courses(self):
            return self.course_list
    
class AttendingDAO:
#Reading the attending.csv file and getting the list 
    def __init__(self):
            self.attending_list=[]
            with open('attending.csv', mode='r')as f:
                for line in f:
                    line=line[:-1]
                    self.course_id, self.student_email = line.split(',')
                    attending =Models.Attending(self.course_id, self.student_email)
                    self.attending_list.append(attending)
        
    def get_attending(self):
            return self.attending_list       

#Getting the list of courses the student registered for    
    def get_student_courses(self, course_list, email):
        stu_course_id=[]
        stu_courses=[]
        for i in self.attending_list:
            if i.get_student_email()==email:
                stu_course_id.append(i.get_course_id())
        for j in stu_course_id:
            for course in course_list:
                if course.get_id()==j:
                    stu_courses.append(course)
        return stu_courses

#Registering the student to a course if he is not already registered for that earlier
    def register_student_to_course(self, email, course_id, course_list):
        s_course_id=[]  
        for attn in self.attending_list:
            if attn.get_student_email()==email:
                s_course_id.append(attn.get_course_id())
        if course_id  in s_course_id:
            print('The course is already in registered list')
            return False
        else:
            for course in course_list:
                if course.get_id()==course_id:
                    self.attending_list.append(Models.Attending(course_id, email))
                    self.save_attending()
            return True

#Rewriting the attending.csv with the new courses added        
    def save_attending(self):
        with open('attending.csv', 'w',newline='') as csvFile:
            writer=csv.writer(csvFile)
            for i in self.attending_list:
                writer.writerow([i.course_id,i.student_email])
        
        
        