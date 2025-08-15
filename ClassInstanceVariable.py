# ClassInstanceVariable
# Class Variable คือ ตัวแปรที่ทำงานภายใน class
# ส่วนอื่นสามารถเข้าถึงขอมูลส่วนนี้ได้เลย (static attribute)
# โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา

# instance Variable คือ ตัวแปรที่อยู่ภายใน object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา


# calss variable
class Employee:
    # class Variable
    __minsalary = 12000
    __maxsalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary,department):
        #  instance Variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def showData(self):
        print('ชื่อพนังงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)



emp1 = Employee('จารุวรรณ', 50000,'วิชาการ')
# print('เงินเดือนขั้นต่ำ = '+str(Employee.__minsalary))
print(Employee._companyName)