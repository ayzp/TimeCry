class Person:
    pass
class Student():
    pass


def main():
    print(Student)

    student1 = Student()
    print(student1)
    print(hex(id(student1)))

    print(isinstance(student1, Person))

    print(type(Student))

if __name__ == '__main__':
    main()
    print(__name__)