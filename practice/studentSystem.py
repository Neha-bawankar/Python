import mysql.connector as mysql

class Student:
    def __init__(self, student_id, name, age, grade):
        self.id = student_id
        self.name = name
        self.age = age
        self.grade = grade

     def __str__(self):
         print(f"{self.id}, name: {self.name}, age: {self.age},grade:{self.grade}")

class StudentRepostiory:
    def __int__(self , db, host, user, password,port):
        self.conn = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = '12345',
            port = 3306
        )
        self.cursor = self.conn.cursor()

    def add_student(self, student:Student):
        sql = ("""insert into student(id, name, age, grade)value(%s, %s, %s, %s)""")
        self.cursor.execute(self, (student.id, student.name, student.age, student.grade))
        print(sql)

    def 