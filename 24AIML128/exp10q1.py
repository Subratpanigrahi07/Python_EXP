# write a parogram to create a class for employee having number data : empid , name , basic pay ,ta,da,gross pay and
#member function : disp () to display the information impliment destructor to reciving memory once use is over , input an emolouyee detail
# where ta =10% of basic pay,da=40% oof basicpay, fross pay=basic pay+ta+da no need to input tada

class Employee:
    def __init__(self, empid, name, basic_pay):
        self.empid = empid
        self.name = name
        self.basic_pay = basic_pay
        
        self.ta = 0.10 * basic_pay
        self.da = 0.40 * basic_pay
        self.gross_pay = basic_pay + self.ta + self.da

    def disp(self):
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Basic Pay:", self.basic_pay)
        print("TA (10%):", self.ta)
        print("DA (40%):", self.da)
        print("Gross Pay:", self.gross_pay)

    def __del__(self):
        print("Memory for Employee {self.name} (ID: {self.empid}) has been released.")

empid = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_pay = float(input("Enter Basic Pay: "))

emp = Employee(empid, name, basic_pay)
emp.disp()

del emp