class Employee:

    raise_amount = 2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


if __name__ == "__main__":
    emp1 = Employee('Ali', 'GholiZadeh', 1000)
    emp2 = Employee('Farahnaz', 'GholiZadeh', 800)
    emp3 = Employee('Amin', 'GholiZadeh', 600)
    emp4 = Employee('Mohammad', 'GholiZadeh', 400)

    print(emp1.email)
    print(emp1.full_name())
    print(emp1.pay)
    emp1.raise_amount = 5
    emp1.apply_raise()
    print(emp1.pay)
