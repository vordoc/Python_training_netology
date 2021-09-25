class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grade_list = []
        for v in self.grades.values():
            for i in v:
                grade_list.append(i)
        result = round(sum(grade_list) / len(grade_list), 2)
        return result

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
              f'{self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершённые курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade = {}

    def average_grade(self):
        grade_list = []
        for v in self.grade.values():
            for i in v:
                grade_list.append(i)
        result = round(sum(grade_list) / len(grade_list), 2)
        return result

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def avg_students_marks(students_list, course_name):
    counter = 0
    mark_sum = 0
    for student in students_list:
        if course_name in student.grades:
            counter += len(student.grades[course_name])
            mark_sum += sum(student.grades[course_name])
    res = round((mark_sum / counter), 2)
    return res


def avg_lecturers_marks(lecturers_list, course_name):
    counter = 0
    mark_sum = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grade:
            counter += len(lecturer.grade[course_name])
            mark_sum += sum(lecturer.grade[course_name])

    res = round((mark_sum / counter), 2)
    return res


some_student = Student('Jesse', 'Pinkman', 'male')
student_1 = Student('Nacho', 'Varga', 'male')
some_student.courses_in_progress += ['Python', 'Java']
some_student.finished_courses += ['Git']
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Git']

some_reviewer = Reviewer('Gale', 'Boetticher')
reviewer_1 = Reviewer('Gustavo', 'Fring')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
reviewer_1.courses_attached += ['Java', 'Python']
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_1.rate_hw(student_1, 'Java', 8)
print(some_student.grades, '\n')
print(student_1.grades, '\n')

some_lecturer = Lecturer('Walther', 'White')
lecturer_1 = Lecturer('Hector', 'Salamanca')
some_lecturer.courses_attached += ['Java', 'Python']
lecturer_1.courses_attached += ['Java', 'Python']
some_student.rate_lecturer(some_lecturer, 'Java', 5)
some_student.rate_lecturer(some_lecturer, 'Python', 8)
some_student.rate_lecturer(lecturer_1, 'Java', 8)
some_student.rate_lecturer(lecturer_1, 'Python', 7)
print(some_lecturer.grade, '\n')
print(lecturer_1.grade, '\n')

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(some_student, '\n')

print(reviewer_1, '\n')
print(lecturer_1, '\n')
print(student_1, '\n')

print(some_student < student_1, '\n')
print(some_lecturer < lecturer_1, '\n')

lecturers_list = [some_lecturer, lecturer_1]
students_list = [some_student, student_1]

print(avg_students_marks(students_list, 'Python'))
print(avg_lecturers_marks(lecturers_list, 'Java'))
