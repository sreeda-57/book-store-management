#bookstore managment system

import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database=
"bookstore")
Cur=con.cursor()

#ADMIN FUNCTIONS
def ADD():
    b_id=int(input("Enter Book Id"))
    b_name=input("Enter Book Name: ")
    genre=input("Genre:")
    quantity=int(input("Enter quantity:"))
    author=input("Enter author name:")
    publication=input("Enter publication house:")
    price=int(input("Enter the price:"))
    Cur.execute("INSERT INTO available_books values ( {},'{}','{}','{}','{}',{},{})" .format(b_id , b_name ,author ,genre , publication,price,quantity))

    con.commit()
    print("+++++++++++++++++++++SUCCESSFULLY ADDED+++++++++++++++++++++")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        ADD()
    if n==2:
        Staff()


def NewStaff():
    staff_id=int(input("Enter staff id :"))
    s_name=input("Enter Fullname :")
    gender= input("Gender(M/F/O):")
    phno=int(input("Staff phone no.:"))
    address=input("Address:")

    Cur.execute(("INSERT INTO staff_rec values ({},'{}','{}','{}','{}')".format(staff_id,s_name,phno,address,gender)))

    con.commit()
    print("++++++++++++++++STAFF IS SUCCESSFULLY ADDED++++++++++++++++++++")

    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        NewStaff()
    if n==2:
        Staff()



def RemoveStaff():
    n=input("Staff Name to Remove: ")
    Cur.execute("DELETE FROM staff_rec WHERE s_name=('{}')".format(n))
    con.commit()
    print("Above Employee is promoted to Customer")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        RemoveStaff()
    if n==2:
        Staff()


def StaffDetail():
    spl_statement= "Select * from staff_rec"
    Cur.execute(spl_statement)
    data=Cur.fetchall()
    for i in data:
        print("************************************")
        print("ID of Employee:", i[0])
        print("Name of Employee:", i[1])
        print("Phone No of Employee", i[2])
        print("Address of Employee:", i[3])
        print("Gender of Employee:", i[4])
        print("************************************")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        StaffDetail()
    if n==2:
        Staff()



def SellRec():
    Cur.execute("select * from sell_rec")
    for j in Cur :
        print("************************************")
        print("Transaction ID : ",j[0])
        print("Buyer ID : ",j[1])
        print("Book ID : ",j[2])
        print("Book Purchased: ",j[3])
        print("Quantity Brought: ",j[4])
        print("Price of Book: ",j[5])
        print("************************************")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        SellRec()
    if n==2:
        Staff()



def TotalRevenue():
    Cur.execute("select sum(price) from sell_rec")
    for x in Cur:
        print("Total Sales Till date",x[0])
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """))
    if n==1:
        TotalRevenue()
    if n==2:
        Staff()


     
def AvailableFS():
    Cur.execute("select * from available_books order by B_name")
    for v in Cur:
        print("************************************")
        print("Book ID: ",v[0])
        print("Book Name: ",v[1])
        print("Book Author: ",v[2])
        print("Book Genre: ",v[3])
        print("Publication House: ",v[4])
        print("Book Price: ", v[5])
        print("Book Available: ",v[6])
    n=int(input("""Want To Continue:
    Yes: 1	
    NO: 2
    OPTION: """ ))
    if n==1:
        AvailableFS()
    if n==2:
        Staff()







#BUYER FUNCTION

def AvailableFU():
    Cur.execute("select * from available_books order by B_name")
    for v in Cur:
        print("************************************")
        print("Book ID: ",v[0])
        print("Book Name: ",v[1])
        print("Book Author: ",v[2])
        print("Book Genre: ",v[3])
        print("Publication House: ",v[4])
        print("Book Price: ", v[5])
        print("Book Available: ",v[6])
        print("************************************")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        AvailableFU()
    if n==2:
        Buyer()


def Purchase():
    trans_id=int(input('Enter transaction ID:  '))
    cusId=int(input("Enter customer ID:"))
    BId=int(input("Enter Book ID:"))
    Bname=input("Enter Book Name:")
    price=int(input("Enter the price:"))
    n=int(input("Enter quantity:"))
    Cur.execute("SELECT quantity FROM available_books WHERE B_name ='{}'"
    .Format(Bname))

    data=Cur.fetchone()
    if data != None:
        if data[0] < n:
           print(n ," books are not available!!!!")
        else:
          Cur.execute("insert into Sell_rec values ({},{},{},'{}',{},{})"  .format(trans_id,cusId,BId,Bname,price,n))

          Cur.execute("update Available_Books set quantity=quantity-{} where B_Name='{}'".format(n,Bname))

          con.commit()
          print("BOOK HAS BEEN SOLD")
    else:
        print("BOOK IS NOT AVAILABLE")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        Purchase()
    if n==2:
        Buyer() 



def UsingName():
     book=input("Enter Book to search:")
     Cur.execute ("select B_name from available_books where  B_name ='{}'"  .format(book))

     t=Cur.fetchone()
     if t!= None:
         print("+++++++++++++++++++++BOOK IS IN STOCK++++++++++++++++++++")
     else:
        print("BOOK IS NOT IN STOCK!!!!!!!")
     n=int(input("""Want To Continue:
     Yes: 1
     NO: 2
     OPTION: """ ))
     if n==1:
         UsingName()
     if n==2:
        Buyer()




def UsingGenre():
        
    g=input("Enter genre to search:")
    Cur.execute("select B_name from available_books where genre='{}'".format(g))
    data=Cur.fetchall()
    if len(data) != 0:
        print("FOLLOWING BOOKS IN THE GENRE", g.upper() ,"ARE AVAILABLE ")
        for rec in data :
            print(rec)
    else:
        print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        UsingGenre()
    if n==2:
        Buyer()



def UsingAuthor():
    o=input("Enter Book's Author to search:")
    Cur.execute("select B_name from available_books where Author='{}'".format(o))
    data=Cur.fetchall()
    if len(data) != 0:
        print("++++++++++++++++++++FOLLOWING ARE THE BOOKS OF THE AUTHOR: ")
        for rec in data :
            print(rec)
            
    else:
        print("BOOKS OF THIS AUTHOR IS NOT IN STOCK!!!!!!!")
    
    n=int(input("""Want To Continue:
    Yes: 1
    NO: 2
    OPTION: """ ))
    if n==1:
        UsingAuthor()
    if n==2:
        Buyer()






def Staff():
    print("1:Add Books")
    print("2.Staff Details")
    print("3.Sell Record")
    print("4.Display Total Revenue")
    print("5.See Available Books")
    print("6.Exit")
    n=int(input("Enter Your Choice: "))
    #To Add Books into the database
    if n==1:
        ADD()
    #Choice For New Staff, Fire staff, View Staff
    elif n==2:
        print("1:New staff entry ")
        print("2:Remove staff ")
        print("3:View existing staff details")
        ch=int(input("Enter your choice: "))
        #NEW STAFF ENTRY
        if ch==1:
            NewStaff()
        #REMOVE STAFF
        elif ch==2:
                RemoveStaff()
        #EXISTING STAFF DETAILS
        else :
            StaffDetail()
    #To See Selling histroy 
    elif n==3:
            SellRec()
    
    #To view total Total Revenue
    elif n==4:
        TotalRevenue()
    #Viewing Available Book As Staff
    elif n==5:
        AvailableFS()
    #Break
    else:
        return



def Buyer():
    print("1.Available Books")
    print("2.Search Books")
    print("3.Purchase Books")
    print("4.Exit")
    r=int(input("Enter Your Choice: "))
    #To See Available Books
    if r==1:
        AvailableFU()
        
    #Searching of books using Name,Genre,Author
    elif r==2:	
        print("1:Search by name")
        print("2:Search by genre")
        print("3:Search by author")
        l=int(input("Search by What : "))
        #Searching Using Name of Book
        if l==1:
            UsingName()
        #Searching Using Genre of Book
        elif l==2:
            UsingGenre()
        #Searching Using Author Name
        else:
            UsingAuthor()
            
    #TO PURCHASE BOOK
    elif r==3:
        Purchase()
    else:
        return 
        
  




#MAIN PROGRAM
            
print("*********************Welcome To  Book Store ******************")
while True :
    print("1.Enter as Employee")
    print("2.Enter as User")
    print("3.Exit")
    ch=int(input(" Enter choice : "))
    if ch==1:
        Staff()
    elif ch==2:
        print("1. Signup")
        print("2. Login")
        s=int(input("Enter Your Choice: "))
        if s==1:
            C_Id=int(input(" Enter customer ID : "))
            C_Name=input(" Enter Name : ")
            PhNo=input(" Enter Phone Number  : ")
            Cur.execute("insert into customer_rec values({},'{}','{}')" .format(C_Id,C_Name,PhNo))
            con.commit()
            print("Sign Up Completed")
        else:
            C_Id=int(input(" Enter customer ID : "))
            Cur.execute("select * from customer_rec where customer_Id={}"
			  .Format (C_Id))
            data=Cur.fetchone()
            if data is not None :
                print("*********************Login Success*****************")
        Buyer()
    else:
        break
        con.close()
