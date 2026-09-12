class student:
    def __init__(self):
        print("This is constructor")
    def __init__(self, name, age):
        self.name="Rizwana"
        self.age=age
    def get_age(self):
        return self.age
stu1=student("Rizwana", 21)
print(stu1.name, stu1.get_age())
