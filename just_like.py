class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        return (f"The name of student is {self.name},\nage of student is {self.age},\ngrade of student is {self.grade}")

st = Student("Khushwant Singh", 17, 84)
print(st.info())