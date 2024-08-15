from student import Student
from group import Group
from group_size_error import GroupSizeError


def student_populator(qty=10):
    student_list = list()
    for i in range(qty):
        gender = 'Male'
        age = 40
        if i % 2 == 0:
            gender = 'Female'
        if i % 3 == 0:
            age = 40 / (i - 5) + 5

        std = Student(gender, age, f'Stevel{i}', f'Jobsec{i}', 'AN142')

        student_list.append(std)

    return student_list


gr = Group('PD1')
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr.add_student(st1)
gr.add_student(st2)
for stud in student_populator(10):
    try:
        gr.add_student(stud)
    except GroupSizeError as e:
        print(e)

assert len(gr.students) <= 10, 'Test1'

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error