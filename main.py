from dbhelper import DBHelper
def main():
    db=DBHelper()
    
    while True:
        print("**********WELCOME**************")
        print()
        print("press 1 to insert new user")
        print("press 2 to display all user")
        print("press 3 to delete  user")
        print("press 4 to update  user")
        print("press 5 to exit  program")
        print()
        try:
            choice= int(input())
            if(choice==1):
                uid=int(input("Enter user id: "))
                username=input("Enter user name: ")
                userphone=input("Enter user phone: ")
                db.insert_user(uid, username, userphone)
                #insert user
                
            elif choice==2:
                db.fetch_all()
                pass
            
            elif choice==3:
                userid=int(input("Enter user di to which you want to delete"))
                db.delete_user(userid)
                
            elif choice==4:
                uid= int(input("Enter id of user: "))
                username=input("Enter new name")
                userphone=input("Enter new phone: ")
                db.update_user(uid, username, userphone)
                
            elif choice==5:
                break
                
            else:
                print("Invalid input try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! try again")
            


if __name__ =="__main__":
    main()
        