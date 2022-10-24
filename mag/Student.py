class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_1 = sum(self.marks) / len(self.marks)
        if marks_1 > 3:
            return True
        else:
            return False