# FnClssObject
# ฟังก์ชันที่ทำงานร่วมกับ class และ object

# isinstance และ die คือฟังก์ชั่นที่ทำงานร่วมกับ ciass และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้างจาก ciass ที่เรานิยามหรือไม่
# dir => แสดง attribute และ method
# __class__ => แสดงชื่อ ciass และ object

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนังงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))


emp1 = Employee('จารุวรรณ', 50000, ';วิชาการ')
emp2 = Employee('สอนรัต', 25000, 'กิจการ')
emp3 = Employee('alther', 10000, 'อาคาร')
emp4 = Employee('plim', 20000, 'HR')

print(isinstance(emp1, Employee)) # ตรวจสอบว่า objb ถูกสร้างจาก ciass ที่ตรวจสอบไหม
print(dir(emp1))
print(emp1.__class__)
