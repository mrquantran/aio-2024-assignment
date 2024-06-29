class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        return f"Student: {self.name}, Year of Birth: {self.yob}, Grade: {self.grade}"


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        return f"Doctor: {self.name}, Year of Birth: {self.yob}, Specialist: {self.specialist}"


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        return f"Teacher: {self.name}, Year of Birth: {self.yob}, Subject: {self.subject}"


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            print(person.describe())

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if teachers:
            return sum(teacher.yob for teacher in teachers) / len(teachers)
        return None


# Tạo đối tượng Ward và thêm người vào
ward = Ward("Ward 1")
ward.add_person(Student("Alice", 2005, "10th Grade"))
ward.add_person(Teacher("Bob", 1980, "Math"))
ward.add_person(Teacher("Carol", 1975, "Science"))
ward.add_person(Doctor("David", 1965, "Cardiology"))
ward.add_person(Doctor("Eve", 1970, "Neurology"))

# Tính trung bình năm sinh của các giáo viên
average_yob = ward.compute_average()
if average_yob is not None:
    print("Average Year of Birth for Teachers:", average_yob)
else:
    print("No teachers in the ward.")
