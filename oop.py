class Employee:
    def __init__(self, name, age, position, employee_id):
        self.name = name
        self.age = age
        self.position = position
        self.employee_id = employee_id

    def display_info(self):
        """Display information about the employee."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Employee ID: {self.employee_id}")
        print()  # Print an empty line for readability


# Create instances of Employee for each employee
abduvali = Employee("Abduvali Murodullayev", 18, "Captain", 2256)
alpomish = Employee("Alpomish Shoymurodov", 18, "Captain", 2256)
oybek = Employee("Oybek Yuldoshev", 17, "Captain", 2256)
