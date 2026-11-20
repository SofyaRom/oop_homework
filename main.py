
# Практическое задание с самопроверкой «Домашнее задание «ООП: наследование, инкапсуляция и полиморфизм»

def average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

    def rate_lecture(self, lecturer, course, grade):
        if (
            not isinstance(lecturer, Lecturer)
            or course not in self.courses_in_progress
            or course not in lecturer.courses_attached
            or type(grade) not in (int, float)
            or not 1 <= grade <= 10
        ):
            return 'Ошибка'

        if course not in lecturer.grades:
            lecturer.grades[course] = []

        lecturer.grades[course].append(grade)

    def average_grade(self):
        all_grades = []

        for grades in self.grades.values():
            all_grades.extend(grades)

        return average(all_grades)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: '
            f'{self.average_grade():.1f}\n'
            f'Курсы в процессе изучения: '
            f'{", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: '
            f'{", ".join(self.finished_courses)}'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []

        for grades in self.grades.values():
            all_grades.extend(grades)

        return average(all_grades)

    def __str__(self):
        return (
            f'{super().__str__()}\n'
            f'Средняя оценка за лекции: {self.average_grade():.1f}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (
            not isinstance(student, Student)
            or course not in self.courses_attached
            or course not in student.courses_in_progress
            or type(grade) not in (int, float)
            or not 1 <= grade <= 10
        ):
            return 'Ошибка'

        if course not in student.grades:
            student.grades[course] = []

        student.grades[course].append(grade)


def average_student_grade(students, course):
    all_grades = []

    for student in students:
        all_grades.extend(student.grades.get(course, []))

    return average(all_grades)


def average_lecturer_grade(lecturers, course):
    all_grades = []

    for lecturer in lecturers:
        all_grades.extend(lecturer.grades.get(course, []))

    return average(all_grades)


if __name__ == '__main__':

    mentor1 = Mentor('Анна', 'Смирнова')
    mentor2 = Mentor('Олег', 'Иванов')

    student1 = Student('Ольга', 'Алёхина', 'Ж')
    student2 = Student('Алексей', 'Соколов', 'М')

    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Мария', 'Петрова')

    reviewer1 = Reviewer('Пётр', 'Петров')
    reviewer2 = Reviewer('Ирина', 'Белова')

    student1.courses_in_progress = ['Python', 'Git']
    student2.courses_in_progress = ['Python', 'Git']

    student1.finished_courses = ['Введение в программирование']
    student2.finished_courses = ['Введение в программирование']

    lecturer1.courses_attached = ['Python']
    lecturer2.courses_attached = ['Python', 'Git']

    reviewer1.courses_attached = ['Python', 'Git']
    reviewer2.courses_attached = ['Python', 'Git']

    print('Проверка наследования:')
    print(isinstance(lecturer1, Mentor))
    print(isinstance(reviewer1, Mentor))

    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer2.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Git', 8)

    reviewer2.rate_hw(student2, 'Python', 8)
    reviewer1.rate_hw(student2, 'Python', 7)
    reviewer2.rate_hw(student2, 'Git', 9)

    student1.rate_lecture(lecturer1, 'Python', 10)
    student2.rate_lecture(lecturer1, 'Python', 8)

    student1.rate_lecture(lecturer2, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Python', 9)
    student1.rate_lecture(lecturer2, 'Git', 10)

    print('\nПроверка ошибок:')

    print(student1.rate_lecture(lecturer1, 'Git', 8))

    print(student1.rate_lecture(reviewer1, 'Python', 8))

    print(student1.rate_lecture(lecturer1, 'Python', 11))

    print(reviewer1.rate_hw(student1, 'Java', 9))

    print(reviewer1.rate_hw(lecturer1, 'Python', 9))

    print(reviewer2.rate_hw(student2, 'Python', 0))

    print('\nИнформация об участниках:')

    participants = [
        mentor1,
        mentor2,
        reviewer1,
        reviewer2,
        lecturer1,
        lecturer2,
        student1,
        student2
    ]

    for participant in participants:
        print(participant)
        print()

    print('Сравнение студентов:')
    print(student1 > student2)   # True
    print(student1 < student2)   # False
    print(student1 == student2)  # False

    print('\nСравнение лекторов:')
    print(lecturer1 > lecturer2)   # True
    print(lecturer1 < lecturer2)   # False
    print(lecturer1 == lecturer2)  # False

    students = [student1, student2]
    lecturers = [lecturer1, lecturer2]

    print('\nСредние оценки по Python:')
    print('Студенты:', average_student_grade(students, 'Python'))
    print('Лекторы:', average_lecturer_grade(lecturers, 'Python'))