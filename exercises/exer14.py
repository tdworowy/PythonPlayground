class Person:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id)


from statistics import mean


class Student(Person):
    rules = {
        "O" : lambda av:  av in range(90, 101),
        "E": lambda av: av in range(80, 90),
        "A": lambda av: av in range(70, 80),
        "P": lambda av: av in range(55, 70),
        "D": lambda av: av in range(40, 55),
        "T": lambda av: av <40
    }
    def __init__(self, first_name, last_name, student_id, scores):
        super().__init__(first_name, last_name, student_id)
        self.scores = scores

    def calculate(self):
        average = mean(self.scores)
        for grade in self.rules:
            if self.rules[grade](int(average)):
                return grade



student = Student("John", "Smith", 1, [100,80,70])
student.calculate()