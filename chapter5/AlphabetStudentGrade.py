class Alphabet_Student_Grade:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade


if __name__ == '__main__':

    student1 = Alphabet_Student_Grade("wunmi", "A")
    student2 = Alphabet_Student_Grade("SON_OF_GOD", "C")
    student3 = Alphabet_Student_Grade("KAYODE", "B")
    student4 = Alphabet_Student_Grade("ORE", "D")
    student5 = Alphabet_Student_Grade("GLORY", "A")

    student_list = [student1, student2, student3, student5]

A = 0
B = 0
C = 0
D = 0

for student in range(student_list):
   if student_list.index(student):
       