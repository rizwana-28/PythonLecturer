class Employee:
    start_time = "9:00 AM" #class attribute
    end_time = "5:00 PM" 

class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject
       
t1 = Teacher("Science")
print(t1.subject,t1.start_time,t1.end_time)


   
