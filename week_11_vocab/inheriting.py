class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self): 
        parent_intro = super().introduce()
        return f"{parent_intro} I study at {self.school}." 

def main():
    student1 = Student("Buddy", 20, "Harvard") #Student1 is an instance of the Student class 
    print(student1.introduce())
    student2 = Student("Bob", "22", "Bunker Hill") #Student2 is an instance of the Student clas
    print(student2.introduce())

if __name__ == "__main__":
    main()
