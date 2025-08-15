# AccessModifier
# คือระดับในการเข้าถึง ciass attribute และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูล และอื่นๆ

# Public คือการประกาศระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใครๆ
# ก็สามารถเข้าถึงและเรียกใช้งานได้

# Protected(_) เป้นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูก
# ที่สืบทอดคุณสมบัติไปใช้เท่านั้น

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มีสิทธิใช้งานได้

class Employee:
    def __init__(self, name, salary, department):


        # Public attribute
        self.name = name
        self.salary = salary
        self.department = department

    # Public method
    def showData(self):
        print('ชื่อพนังงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))


emp1 = Employee('จารุวรรณ', 50000, ';วิชาการ')
emp1.salary = 51000
emp1.showData()
