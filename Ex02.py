# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attributbute และ Method ดังนี้
# attribute
#   name เป็นชื่อของบุคคล
#   age เป็นอายุของบุคคล
# method
#   Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ
#   My name is <name>.I'm <age> year old

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        print('My name is {}. I\'m {} year old'.format(self.name, self.age))

student = people('จารุวรรณ', 25)
student.Introduce()