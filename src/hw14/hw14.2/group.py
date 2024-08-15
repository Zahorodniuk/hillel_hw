from group_size_error import GroupSizeError


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
        return f'Group: {self.number}\n{all_students}'
