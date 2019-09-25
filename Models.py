class Student:
#Initialize attributes of Student class
    def __init__(self, email, s_name, s_password):
        self.s_name=s_name
        self.email=email
        self.s_password=s_password
        
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.s_password
    
class Course:
#Initialize attributes of Course class
    def __init__(self,c_id,c_name,instructor):
        self.c_id=c_id
        self.c_name=c_name
        self.instructor=instructor 
        
    def get_id(self):
        return self.c_id
    
    def get_name(self):
        return self.c_name
    
    def get_instructor(self):
        return self.instructor
    
class Attending:
#Initialize attributes of Attending class
    def __init__(self, course_id, student_email):
        self.course_id=course_id
        self.student_email=student_email
   
    def get_course_id(self):
        return self.course_id
    
    def get_student_email(self):
        return self.student_email

