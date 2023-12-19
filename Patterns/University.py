class UniversitySingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, university_name):
        self.university_name = university_name
        self.departments = {}

    def add_department(self, department_name, head_of_department):
        if department_name not in self.departments:
            self.departments[department_name] = {
                'head': head_of_department,
                'courses': []
            }
            print(f"Department '{department_name}' added to {self.university_name}")
        else:
            print(f"Department '{department_name}' already exists in {self.university_name}")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed from {self.university_name}")
        else:
            print(f"Department '{department_name}' does not exist in {self.university_name}")

    def add_course_to_department(self, department_name, course_name):
        if department_name in self.departments:
            self.departments[department_name]['courses'].append(course_name)
            print(f"Course '{course_name}' added to department '{department_name}'")
        else:
            print(f"Department '{department_name}' does not exist in {self.university_name}")

    def list_departments(self):
        print(f"Departments in {self.university_name}:")
        if self.departments:
            for department, info in self.departments.items():
                print(f"{department}: Head - {info['head']}, Courses - {', '.join(info['courses'])}")
        else:
            print("No departments available")


if __name__ == "__main__":
    university1 = UniversitySingleton("ABC University")
    university2 = UniversitySingleton("XYZ University")

    print(f"University 1 ID: {id(university1)}")
    print(f"University 2 ID: {id(university2)}")

    university1.add_department("Computer Science", "Dr. Smith")
    university2.add_department("Physics", "Prof. Johnson")
    university1.add_department("Computer Science", "Dr. Brown")
    university1.add_course_to_department("Computer Science", "Python Programming")
    university2.add_course_to_department("Physics", "Quantum Mechanics")

    university1.list_departments()
    university2.list_departments()

    university2.remove_department("Physics")
    university1.list_departments()
    university2.list_departments()


print("End of the program")
