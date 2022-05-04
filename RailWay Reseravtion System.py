import os,sys
from time import sleep
import pandas as pd
import mysql.connector as mc

c=mc.connect(host='localhost',user='root',password='kartik',database='rail')
cr=c.cursor()
sql="select PNR from passengers"
cr.execute(sql)
res=sorted(cr.fetchall())
if(res):
    no = res[len(res)-1]
    pnr=no[0]
else:
    pnr=1001



#$$$$$$$$$$$$$$$$ EXTRA Funtions $$$$$$$$$$$$$$$$$$$
    
def clear():
    os.system('cls')



#~~~~~~~~~~ Starting Window ~~~~~~~~~~~~~~~    
def window():
    clear()
    loading()
    welcome = "WELCOME TO THE"
    railway = "RAILWAY RESERVATION SYSTEM"
    print("\n\n\n\n\n\t\t\t\t",end="")
    ani(welcome)
    print("\n\n\t\t\t\t\t",end="")
    ani(railway)
    ani("\n\n\n\nPress Enter to Continue.....")    
    a=input()
    menu()

    
#~~~~~~~~~~ Animation ~~~~~~~~~~~~~~~   
def ani(value,t=0.001):
    for j in value:
        print(j,end="")
        sys.stdout.flush()
        sleep(t)

#~~~~~~~~~~ Loading  ~~~~~~~~~~~~~~~   
def loading(t=1):
    load=['|', '/', '-', '\\']
    a=0
    while(a<t):
        for j in range(4):
            clear()
            print("Loading..",end="")
            print(load[j])
            sleep(0.1)
        a+=1
    clear()


#~~~~~~~~~~ Continue ~~~~~~~~~~~~~~~   
def conti():
    ani("\n\nPress Enter to Continue...")
    a=input()
 


#~~~~~~~~~~ Header  ~~~~~~~~~~~~~~~   
def header():
    print("\n\t\t\t\t*******************************************")
    print("\t\t\t\t\t     Railway Reservation ")
    print("\t\t\t\t*******************************************")
    sleep(0.3)


#~~~~~~~~~~ Star Printing ~~~~~~~~~~~~~~~   
def star():
    print("\t\t\t\t*******************************************")


#~~~~~~~~~~ End Printing ~~~~~~~~~~~~~~~   
def end():
    print("\t\t\t\t--------------------------------------------")
    print("\t\t\t\t--------------------------------------------")


#~~~~~~~~~~ Style Printing ~~~~~~~~~~~~~~~   
def style():
    print("\n\t\t\t\t\t_____________________________________________")
    print("\t\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    
#----------------------- Main Menu ---------------------------------
def menu():
    clear()
    header()
    print("\t\t\t\t\t      1.User Loging")
    sleep(0.3)
    print("\t\t\t\t\t      2.Admin Loging")
    sleep(0.3)
    print("\t\t\t\t\t      3.Quit")
    sleep(0.3)
    print("\t\t\t\t--------------------------------------------")
    print("\t\t\t\t--------------------------------------------")
    n=int(input("Enter Your Choice :- "))
    if (n==1):
        clear()
        user()
    elif (n==2):
        clear()
        log=[]
        userid=input("Choose Username :- ")
        psw = input("Enter Password :- ")
        log.append(userid)
        log.append(psw)
        login=tuple(log)
        sql="Select username,password from admin;"
        cr.execute(sql)
        result=cr.fetchall()
        if(login in result):
            adminmenu()
        else:
            print("\t\tInvalid Credentials")
            menu()
    elif(n==3):
        clear()
        ani("\n\n\t\t\tThank You...")
        ani("\n\n\t\t\t\t\tHave a Good Day")
        sleep(2)
        exit()
    else:
        clear()
        print("Chosse Correct options")
        menu()

#-------------------------- User Login Section -----------------------
def user():
    value=[]
    print("\n\t\t\t\t*******************************************")
    print("\t\t\t\t\t 1.Loging Account")
    sleep(0.3)
    print("\t\t\t\t\t 2.Create Account")
    sleep(0.3)
    print("\t\t\t\t\t 3.Go Back")
    sleep(0.3)
    end()
    n=int(input("Enter Your Choice :- "))
    if (n==1):
        clear()
        log=[]
        ani("\n\t\t\t\t# # # # # # # # # # # # # # # # # # # # # #",0.001)
        userid=input("\n\n\t\t\t\t\tEnter Username :- ")
        sleep(0.2)
        clear()
        print("\n\t\t\t\t# # # # # # # # # # # # # # # # # # # # # #")
        sleep(0.2)
        psw = input("\n\t\t\t\t\tEnter Password :- ")
        clear()
        log.append(userid)
        log.append(psw)
        login=tuple(log)
        sql="Select userid,pass from login;"
        cr.execute(sql)
        result=cr.fetchall()
        if(login in result):
            loading(1)
            clear()
            usermenu()
        else:
            clear()
            print("\n\t\t------------------------------")
            print("\t\t--> Invalid Credentials")
            print("\t\t------------------------------")
            ani("Enter to Continue...")
            a=input()
            clear()
            user()
    elif (n==2):
        clear()
        ani("\n\t\t\t\t--------------------------------------",0.001)
        name=input("\n\n\t\t\t\t\tEnter Your Name :- ")
        clear()
        print("\n\t\t\t\t--------------------------------------")
        userid=input("\n\n\t\t\t\t\tChoose Username :- ")
        sql = "select userid from login"
        cr.execute(sql)
        res  = cr.fetchall()
        res = str(res)
        if userid in res:
            ani("\n\t-->Username Already Exist....")
        else:
            clear()
            print("\n\t\t\t\t--------------------------------------")
            psw = input("\n\n\t\t\t\t\tEnter Password :- ")
            clear()
            value.append(userid)
            value.append(psw)
            value.append(name)
            sql="insert into login(userid,pass,name)values(%s,%s,%s)"
            cr.execute(sql,value)
            c.commit()
            ani("\n\t-->Account Created You Can Login")
        conti()
        clear()
        user()
    elif(n==3):
        menu()
    else:
        clear()
        ani("\n\t\t--> Chosse Correct options..")
        conti()
        clear()
        user()
        

#--------------- User Menu Section --------------------------
def usermenu():
    header()
    print("\t\t\t\t\t      1.PNR status")
    sleep(0.1)
    print("\t\t\t\t\t      2.Reservation of Ticket")
    sleep(0.1)
    print("\t\t\t\t\t      3.Cancellation of Ticket")
    sleep(0.1)
    print("\t\t\t\t\t      4.Train List")
    sleep(0.1)
    print("\t\t\t\t\t      5.Logout")
    sleep(0.1)
    end()
    n=int(input("|Enter Your Choice :-  "))
    if(n==1):
        displayPNR()
    elif(n==2):
        reservation()
    elif(n==3):
        cancel()
    elif(n==4):
        train_list()
    elif(n==5):
        menu()
    else:
        clear()
        ani("\n\t\t--> Chosse Correct options..")
        conti()
        clear()
        usermenu()
    conti()
    clear()
    usermenu()

#--------------- Admin Menu Section --------------------------

def adminmenu():
    loading()
    clear()
    header()
    print("\t\t\t\t\t      1.Train Detail")
    print("\t\t\t\t\t      2.show all passengers")
    print("\t\t\t\t\t      3.Exit")
    end()
    n=int(input("| Enter Your Choice --> "))
    if(n==1):
        traindetail()
    elif(n==2):
        passenger()
    elif(n==3):
        menu()
    else:
        print("wrong choice")


#______________________________ Update  ____________________
def update():
    sql = "select train_no from train_details"
    cr.execute(sql)
    tn_list = str(cr.fetchall())
    clear()
    train_list()
    lst=[]
    print("\t\t| For Adding New Train Details Press A..")
    print("\t\t| For Updating Existing Train Details Press U..")
    print("\t\t| Press B For GO-Back")
    op = input().upper()
    if(op == 'U'):
        star()
        num = int(input("| Enter Train No. :-  "))
        tno='('+str(num)+',)'
        if(tno in tn_list):
            clear()
            train_list()
            ani("\n\t| Update Option ...")
            print("\n\t 1.Arrival Time ")
            print("\t 2.Depature Time")
            print("\t 3.Route")
            op = int(input("| Choose Option -> "))
            if(op==1):
                arrival=input("| Enter New Arrival Time of Train :-  ")
                sql = 'update train_details set arrival_time = "'+arrival+'" where train_no = '+str(num)+';'
                cr.execute(sql)
                c.commit()
                print("Update Succesfull...")
            elif(op==2):
                departure=input("| Enter New Departure Time of Train :-  ")
                sql = 'update train_details set Departure_Time = "'+departure+'" where train_no = '+str(num)+';'
                cr.execute(sql)
                c.commit()
                print("Update Succesfull...")
            elif(op==3):
                route=input("| Enter New Route of Train :-  ")
                sql = 'update train_details set route = "'+route+'" where train_no = '+str(num)+';'
                cr.execute(sql)
                c.commit()
                print("Update Succesfull...")
                sleep(0.1)
            else:
                ani('-> Choose Correct Option...')
                conti()
        else:
            print("| Enter Correct Train No..")
        update()
    elif(op=='A'):
        sql='select Sr_no from train_details;'
        cr.execute(sql)
        res=cr.fetchall()
        tno = int(input("| Enter Train No. :-  "))
        num = '('+str(tno)+',)'
        if(num in tn_list):
            print("\t\t| Train No. Already Exist...")
            conti()
            update()
        sr_no = list(res[-1])[0]+1
        Tname=input("| Enter Train Name. :-  ")
        arrival=input("| Enter Arrival Time of Train :-  ")
        depature =input("| Enter Depature Time of Train :-  ")
        clear()
        ani('| Route Name Seprate with Commas |\n')
        route=input("| Enter Route of Train :-  ")
        lst.append(sr_no)
        lst.append(tno)
        lst.append(Tname)
        lst.append(arrival)
        lst.append(depature)
        lst.append(route)
        sql="insert into train_details values(%s,%s,%s,%s,%s,%s)"
        cr.execute(sql,lst)
        c.commit()
        clear()
        train_list()
        ani("\n\t\t\t| Add Sucessfully....")
        sleep(0.1)
        conti()
        traindetail()
    elif(op=="B"):
        traindetail()
    else:
        print("| Wrong Input...")
        conti()
        update()
   
    
    











#--------------------- Train Details Section ----------------------------
def traindetail():
    clear()
    star()
    print("\t\t\t\t\t      1.Train List")
    print("\t\t\t\t\t      2.Update Train")
    print("\t\t\t\t\t      3.Go Back")
    star()
    n=int(input("| Enter Your Choice --> "))
    if(n==1):
        train_list()
    elif(n==2):
        update()
    elif(n==3):
        adminmenu()
    conti()
    clear()
    adminmenu()











#================================== Train List ======================================
def train_list():
    clear()
    star()
    print("\t\t\t\t\t      Train Details")
    star()
    sql="select * from train_details order by Sr_no"
    cr.execute(sql)
    res=cr.fetchall()
    print('| Sr.No | Train No | Arrival Time | Depature Time | Train Name | Route | ')
    for i in range(len(res)):
        sr=         str(res[i][0]).rjust(6)
        no =        str(res[i][1]).center(15)
        arrival =   str(res[i][3]).center(10)
        depature =  str(res[i][4]).center(15)
        name =      str(res[i][2]).center(15)
        route =     str(res[i][5]).center(10)
        print(sr,no,arrival,depature,name,route)
    print('\n')















#--------------------------------- Passengers List Section ------------------------------
def passenger():
    clear()
    print("_____________________________________________________________________________________________________________________")
    print("Passenger List".center(100))
    print("_____________________________________________________________________________________________________________________")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sql="select * from passengers"
    cr.execute(sql)
    raw=cr.fetchall()
    results = pd.read_sql_query(sql,c)
    results.to_csv("output.csv", index=False)
    df = pd.read_csv('output.csv')
    print(df)
    file = 'output.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
    conti()
    clear()
    adminmenu()

def date_fun():
    clear()
    month = input("\t| Enter Month -> ")
    day = input("\t| Enter Date -> ")
    year = input("\t| Enter Year -> ")
    fdate = year+'-'+month+'-'+day
    return fdate















#--------------------- Ticket Reservation Section ----------------------
def reservation():
    global pnr
    pnr = pnr+1
    l1=[]
    clear()
    ani("\n\t\t\t\t Please Enter Data Correctfully...\n")
    sleep(0.3)
    pname=input("\n\t| Enter passenger Name -> ").upper()
    age=input("\t| Enter age of Passenger -> ")
    gen = input("\t| Gender M | F -> ").upper()
    date = date_fun()
    clear()
    place=station()
    _from=place[0]
    _to=place[1]
    clear()
    tsql = "select * from train_details where route like '%"+_from+"%"+_to+"%'"
    cr.execute(tsql)
    res = cr.fetchall()
    print('\n')
    loading()
    if(res):
        print('| Train No | Arrival Time | Depature Time | Train Name | Route | ')
        for i in range(len(res)):
                no =        str(res[i][1]).center(15)
                arrival =   str(res[i][3]).center(10)
                depature =  str(res[i][4]).center(15)
                name =      str(res[i][2]).center(15)
                route =     str(res[i][5]).center(10)
                print(no,arrival,depature,name,route)
    else:
        print("\n\t| NO Direct Train.....")
        conti()
        clear()
        usermenu()
    print('\n')
    trainno=input("\t| Enter Train number -> ")
    clear()
    sql = "select train_name from train_details where train_no ="+str(trainno)+";"
    try:
        cr.execute(sql)
    except:
        clear()
        print("\n\t| -> Please Enter Valid Data.....")
        conti()
        clear()
        usermenu()
    res = cr.fetchall()
    train_name= res[0][0]
    ani("\nSelect a Class you would like to travel in")
    ani("\n1.AC FIRST CLASS")
    ani("\n2.AC SECOND CLASS")
    ani("\n3.AC THIRD CLASS")
    ani("\n4.SLEEPER CLASS")
    cp=int(input("\n\n\t| Enter your choice -> "))
    if(cp==1):
        amt=1000
        cls='1A'
        coach = 'A'
    elif(cp==2):
        amt=800
        cls='2A'
        coach = 'B'
    elif(cp==3):
        amt=500
        cls='3A'
        coach = 'C'
    else:
        amt=350
        cls='Sls'
        coach = 'S'
    
    seat=seat_fun(coach)
    l1.append(pnr)
    l1.append(pname)
    l1.append(age)
    l1.append(trainno)
    l1.append(cls)
    l1.append(seat)
    l1.append(amt)
    l1.append(gen)
    l1.append(date)
    l1.append(_from)
    l1.append(_to)
    sql="insert into passengers(PNR,Pname,Age,Train_no,Coach,seat,Amount,Gender,Journey_Date,_from,_to)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cr.execute(sql,l1)
    except:
        clear()
        print("\n\t| -> Please Enter Valid Data.....")
        conti()
        clear()
        usermenu()
    c.commit()
    print('\n')
    clear()
    loading()
    title ="Your Ticket"
    ticket(pnr,pname,age,trainno,cls,amt,gen,seat,date,_from,_to,title,train_name)
    print('\n')
    usermenu()
















#$$$$$$$$$$$$$$$$$$$$$$$ SEATS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def seat_fun(coach):
    sql='select seat from passengers where seat like "'+coach+'%"'
    cr.execute(sql)
    res=cr.fetchall()
    ac1 = []
    ac2 = []
    ac3 = []
    slp = []
    if(res):
        for j in res:
            i = j[-1]
            if('A' in i):
                ac1.append(i)
            elif('B' in i):
                ac2.append(i)
            elif('C' in i):
                ac3.append(i) 
            elif('S' in i):
                slp.append(i)
                
    if(res):
        if(coach == 'A'):
            ref = ac1[-1]
        elif(coach == 'B'):    
            ref = ac2[-1]
        elif(coach == 'C'):       
            ref = ac3[-1]
        elif(coach == 'S'):            
            ref = slp[-1]
        number = int(''.join([i for i in ref if i.isdigit()]))
        position = number+1
        coach = coach
        seat = str(coach)+'/'+str(position)
    else:
        coach=coach
        position=1
        seat = str(coach)+'/'+str(position)
    return seat


















#++++++++++++++++++++++++ Station Choosing +++++++++++++++++++++++++
def station():
    clear()
    ani("\n\t| Choose Station...")
    print("\n\t 1.Delhi")
    print("\t 2.Gujrat")
    print("\t 3.Kolkata")
    print("\t 4.Goa")
    print("\t 5.Mumbai")
    print("\t 6.Chennai")
    print("\t 7.Punjab")
    print("\t 8.Kerla")
    print("\t 9.Karnataka")
    print("\t 10.Maharashtra")
    ch=int(input("\t| From -> "))
    if(ch==1):
        _from='Delhi'
    elif(ch==2):
        _from='Gujrat'
    elif(ch==3):
        _from="Kolkata"
    elif(ch==4):
        _from='Goa'
    elif(ch==5):
        _from='Mumbai'
    elif(ch==6):
        _from='Chennai'
    elif(ch==7):
        _from='Punjab'
    elif(ch==8):
        _from='Kerla'
    elif(ch==9):
        _from='Karnataka'
    elif(ch==10):
        _from='Maharashtra'
    else:
        ani("\t-> Choose Station From Given List..\n")
        station()
    ch2=int(input("\t| To -> "))
    if(ch==ch2):
        print("\t-> You cannot Choose Same Stations...\n")
        station()
    elif(ch2==1):
        _to='Delhi'
    elif(ch2==2):
        _to='Gujrat'
    elif(ch2==3):
        _to="Kolkata"
    elif(ch2==4):
        _to='Goa'
    elif(ch2==5):
        _to='Mumbai'
    elif(ch2==6):
        _to='Chennai'
    elif(ch2==7):
        _to='Punjab'
    elif(ch2==8):
        _to='Kerla'
    elif(ch2==9):
        _to='Karnataka'
    elif(ch2==10):
        _to='Maharashtra'
    else:
        ani("\t-> Choose Station From Given List..\n")
        station()
    return _from,_to
        









    
#====================  Printing Ticket ==============================
def ticket(pnr,pname,age,trainno,cls,amt,gen,seat,date,_from,_to,title,train_name):
    print("\n","Ticket Confirmed".center(110))
    print("\t\t\t____________________________________________________")
    print("\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\t\t\t",pname.center(50))
    print("\t\t\t","PNR:",pnr,"Age:".rjust(14),age,"Amount:".rjust(15),amt)
    print("\t\t\t","Seat:",seat,"Class:".rjust(16),cls,"Trn:".rjust(10),trainno)
    print("\t\t\t","Date:",date,"From:".rjust(8),_from,"To:".rjust(5),_to)
    print("\t\t\t",train_name.center(50))
    print("\t\t\t____________________________________________________")
    print("\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    conti()
    clear()










#---------------------- Ticket Cancellation Section ----------------------------
def cancel():
    sql="select PNR from passengers"
    cr.execute(sql)
    res=cr.fetchall()
    Confirm = False
    clear()
    loading()
    print("\n")
    star()
    print("\t\t\t\t\t     Ticket Cancellation")
    star()
    pn=int(input("| Enter PNR Number -> "))
    pnr=(pn,)
    if(pnr in res):
        sql="delete from passengers where pnr=%s;"
        cr.execute(sql,pnr)
        c.commit()
        Confirm = True
    else:
        print("Invalid Number !! ")
        conti()
    if(Confirm):
        clear()
        loading(1)
        style()
        print("\t\t\t\t\t               Ticket Cancelled           ")
        conti()
    print('\n')
    clear()
    usermenu()









#---------------------- PNR Checking Section -----------------------
def displayPNR():
    Confirm = False
    sql="select PNR from passengers"
    cr.execute(sql)
    res=cr.fetchall()
    clear()
    print("\n")
    star()
    print("\t\t\t\t\t     PNR Checking")
    star()
    pn=int(input("| Enter PNR number --> "))
    pnr=(pn,)
    if(pnr in res):
        Confirm = True
    else:
        print("Invalid Number !! ")
        conti()
    if(Confirm):
        sql="select * from passengers where pnr=%s"
        cr.execute(sql,pnr)
        res=cr.fetchall()
        pnr=res[0][0]
        pname=res[0][1]
        age=str(res[0][2])
        trainno=res[0][3]
        cls=res[0][4]
        seat=res[0][5]
        amt=res[0][6]
        gen=str(res[0][7])
        date = str(res[0][8])
        _from =res[0][9]
        _to=res[0][10]
        sql = "select train_name from train_details where train_no ="+str(trainno)+";"
        cr.execute(sql)
        res = cr.fetchall()
        train_name= res[0][0]
        clear()
        loading(0)
        title="Ticket Confirmed"
        ticket(pnr,pname,age,trainno,cls,amt,gen,seat,date,_from,_to,title,train_name)
    print("\n")
    clear()
    usermenu()




#----------------------------- Starting Section -----------------------------
__name__
window()


