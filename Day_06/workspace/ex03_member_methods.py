class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.dept = kwargs.get('dept')
        self.salary = kwargs.get('salary')

    def print(self):
        print('===== EMPLOYEE =====')
        print(f'Name      : {self.name}')
        print(f'Department: {self.dept}')
        print(f'Salary    : Rs.{self.salary}')
        print("--------------------")


def main():
    e1 = Employee(name='Kishore', dept='ADMIN', salary=45000, email='kishore@xmpl.com')
    e2 = Employee(name='Kiran', salary=37000)
    e1.print()  # print() function is called by python which passes e1 as the first argument
    e2.print()
    # Employee.print(e2)

    e2.dept = 'ACCOUNTING'
    e2.print()

main()
