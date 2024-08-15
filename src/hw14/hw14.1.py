class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name}, {self.last_name}'




class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name}, {self.last_name}, {self.record_book}'


class GroupSizeError(Exception):
    def __init__(self, message="The size of the group exceeds the limit!"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupSizeError()
        self.students.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.students)
        return f'Number: {self.number}\n{all_students}'


def student_populator(qty=10):
    studentList = list()
    for i in range(qty):
        gender = 'Male'
        age = 40
        if i % 2 == 0:
            gender = 'Female'
        if i % 3 == 0:
            age = 40 / (i - 5) + 5

        std = Student(gender, age, f'Stevel{i}', f'Jobsec{i}', 'AN142')

        studentList.append(std)

    return studentList

gr = Group('PD1')
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr.add_student(st1)
gr.add_student(st2)
for std in student_populator(10):
    try:
        gr.add_student(std)
    except GroupSizeError as i:
        print(i)

assert len(gr.students) <= 10, 'Test1'

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error



