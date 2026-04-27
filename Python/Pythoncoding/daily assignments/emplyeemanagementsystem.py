class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.__employee_id}")
        print(f"Employee Name: {self.__name}")
        print(f"Salary: {self.__salary}")

    def give_salary_hike(self, percentage):
        if percentage > 0:
            hike_amount = (self.__salary * percentage) / 100
            self.__salary += hike_amount
        else:
            print("Invalid percentage. Salary hike must be positive.")


if __name__ == "__main__":
    employee1 = Employee(employee_id="E123", name="Alice", salary=50000.0)
    employee1.display_employee_info()
    employee1.give_salary_hike(10)
    employee1.display_employee_info()
    employee1.give_salary_hike(-5)