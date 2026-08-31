class InvalidSalaryException(Exception):
    pass


salary = input("Enter salary: ")
salary = float(salary)

if salary<15000 or salary>1000000:
    raise InvalidSalaryException("Salary must be between Rs.15000 and Rs.1000000")

print("You have entered a valid salary.")