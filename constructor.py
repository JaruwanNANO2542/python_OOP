# constructor
    # เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
    # โครงสร้าง constructor
        # def __init__(self):
        #      pass

# destructor
# เป็น method พิเศษที่ตรงข้างหน้า constructor จะถูกใช้งานเมื่อ
# สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย object
# ส่วนใหญจะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โครงสร้าง
# def __del__(self):
#   pass

# การสร้าง constructor

class Employee:
    def __init__(self, name, salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนังงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))
    # มีหรือไม่มีก็ได้ destructor
    def __del__(self):
        print('call destructor')

emp1 = Employee('จารุวรรณ', 50000,';วิชาการ')
emp1. showData()

emp2 = Employee('สอนรัต', 25000,'กิจการ')
emp2. showData()

emp3 = Employee('alther', 10000,'อาคาร')
emp3. showData()

emp4 = Employee('plim', 20000,'HR')
emp4.salary = 21000
emp4. showData()