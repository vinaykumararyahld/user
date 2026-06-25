from school_back import school_manage

def student_main():
    school=school_manage()
    
    while True:
        print("**************STUDENT DATA**********************")
        print()
        print("Press 1 to Insert student data")
        print("Press 2 to see all student data")
        print("Press 3 to delete any student data")
        print("Press 4 to update any student data")
        print("Press 5 to selective student data")
        print("Press 6 to EXIT ")
        print()
        try:
            choice=int(input())
            if(choice==1):
                studentid=int(input("Enter Studentid : "))
                studentname=input("Enter studentname :")
                studentclass=int(input("Enter studentclass :"))
                school.insert_students(studentid, studentname, studentclass)
                
            elif(choice==2):
                school.fetch_all()

            elif(choice==3):
                studentid=int(input("Enter the studentid which you to delete :"))
                school.delete_student(studentid)
                
            elif(choice==4):
                studentid=int(input("Enter studentid for update :"))
                studentname=input("Enter student new name :")
                studentclass= input("Enter Student new class: ")
                school.update_student(studentid, studentname, studentclass)
                
            elif(choice==5):
                studentid=int(input("Enter studentid : "))
                school.fetch_select(studentid)

            elif(choice==6):
                break
            
            else:
                print("Invail Entry try again ! ")
        except Exception as e:
            print(e)
            print("Enty is invaild please try again ! ")
            
if __name__ =="__main__":
    student_main()
                    
                
            
           
    

