import mysql.connector as connector
class school_manage:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='Vinay@1998',
                                   database='pythontest')
        query = 'create table if not exists students(studentid int primary key , studentname varchar(50), studentclass int  )'
        cur=self.con.cursor()
        cur.execute(query)
        print("Table created")
        
        # Student insert section coding
        
    def insert_students(self, studentid , studentname, studentclass):
        query ="insert into students(studentid, studentname, studentclass) values({},'{}',{})".format(studentid,studentname,studentclass)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student data upload")
        
        
    def fetch_all(self):
        query="select * from students"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Student ID : ", row[0]) 
            print("Student Name : ", row[1])
            print("Student Class : ", row[2])
            print()
            print()
            
    def fetch_select(self, studentid):
        query="select * from students where studentid = {}".format(studentid)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Student ID : ", row[0]) 
            print("Student Name : ", row[1])
            print("Student Class : ", row[2])
            print()
            print()
            
            
    def delete_student(self,studentid):
        query="delete from students where studentid = {}".format(studentid)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Student deleted")

    def update_student(self, studentid, newstudentname, newstudentclass ):
        query="update students set studentname = '{}', studentclass = {} where studentid= {}".format(newstudentname,newstudentclass, studentid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student updated")