class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"大家好，我叫: {self.name}, 今年: {self.age}岁，是: {self.gender}生。"
    
class Student(Person):
    def __init__(self, name, age, gender, student_id, grade):
        super().__init__(name, age, gender)
        self.grade = grade
        self.student_id = student_id
        self.course = []

    def introduce(self):
        return f"大家好，我叫: {self.name}, 今年: {self.age}岁，是: {self.gender}生，学号: {self.student_id}，在读: {self.grade}级。"
    
    def enroll_course(self, course):
        if course not in self.course:
            self.course.append(course)
            course.add_student(self)
            return f"{self.name}成功报名了: {course.name}课程。"
        return f"{self.name}已经报名了: {course.name}课程。"
    
    def list_courses(self):
        if self.course:
            course_names = [course.name for course in self.course]
            return f"{self.name}已经报名的课程有:{','.join(course_names)}"
        else:
            return f"{self.name}没有报名任何课程。"

class Administrator(Person):
    def __init__(self, name, age, gender, staff_id):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.course = []

    def introduce(self):
        return f"大家好，我叫: {self.name}, 今年: {self.age}岁，是: {self.gender}生，工号: {self.staff_id}。"

class Grade:
    def __init__(self, grade):
        self.grade = grade
        self.course = []

    def add_course(self, course):
        if course not in self.course:
            self.course.append(course)
            return f"成功添加课程: {course.name}。"
        return f"课程: {course.name}已经添加过了。"

    def list_courses(self):
        return [course.name for course in self.course]
    
    def introduce(self):
        return f"课程：{self.course.name}，成绩为: {self.course.grade}。"
