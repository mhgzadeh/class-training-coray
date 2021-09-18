class Employee:
    __id = 0
    __raise_amount = 2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.id = self.id_counter()
        # self.email = self.first + self.last
        # self.email = first + "." + last + '@company.com'

    @classmethod
    def id_counter(cls):
        cls.__id += 1
        return cls.__id

    @property
    def email(self):
        return self.first + self.last + '@company.com'

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def fullname(self, name):
        first, last = name.spilit(' ')
        self.first = first
        self.last = last

    # @full_name.deleter
    # def fullname(self):
    #     print("Delete Name! ")
    #     self.first = None
    #     self.last = None

    def apply_raise(self):
        self.pay = self.pay * self.__raise_amount

    @classmethod
    def pay_checker(cls, first, last, pay):
        if pay < 700:
            print(f'chrage your account')
            return f'Not acceptable user .'
        else:
            pay += 25
            print('account successfully created.')
            return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __add__(self, other):
        return self.pay + other.pay

    def __str__(self):
        return f"Emploee {self.id}"


class Developer(Employee):

    def __init__(self, first, last, pay, pro_lan):
        super().__init__(first, last, pay)
        self.pro_lan = pro_lan


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


if __name__ == "__main__":
    emp1 = Employee.pay_checker('Mohammad', 'GholiZadeh', 800)
    emp2 = Employee.pay_checker('Ali', 'GholiZadeh', 1000)
    emp3 = Employee.pay_checker('Farahnaz', 'GholiZadeh', 900)
    dev1 = Employee.pay_checker('Amin', 'GholiZadeh', 1100)
    dev2 = Developer('Mahmud', 'Tinati', 100, 'Java')
    dev3 = Developer('reza', 'rezaie', 100, 'Java')

    mgr1 = Manager('Masume', 'Abassgholizadeh', 1500, [dev1])

    emp1.full_name = 'Mohammad'
    print(emp1.full_name)
    
    # del dev2.full_name
    # print(dev2.full_name)
