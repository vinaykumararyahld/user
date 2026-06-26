import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='pass. that you call your sql pass',
                                   database='pythontest')
        query='create table if not exists user(userId int primary key, username varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

        
    #insert
    def insert_user(self, userid, username,phone ):
        query = "insert into user(userid,userName, phone) value({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user save to db")
        
    #fetch all
    def fetch_all(self):
        query = "select * from user"
        cur =self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user Id :", row[0])
            print("user name :", row[1])   
            print("user phone :", row[2])           
            print()
            print()
      #delete user      
    def delete_user(self,userId):
        query= "delete from user where userId= {}".fromat(userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")
        
    #update or up to date
    
    def update_user(self, userId, newName , newPhone):
        query ="update user set username = {}, phone = {}where userId ={}".format(newName, newPhone, userId)
        print(query)
        cur =self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
        
  
