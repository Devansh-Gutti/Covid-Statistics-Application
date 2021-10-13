#This project aims to enhance the public knowledge of the COVID-19 pandemic through the application of a Python-SQL connector database
#_________________________________________________________________________________________________________________________________________________


import mysql.connector
from prettytable import PrettyTable
mydb=mysql.connector.connect(host="localhost", user="root", passwd="root")
cur=mydb.cursor(buffered=True)

def pretty():                                         #pretty table
    print("Data in table is:")
    cur.execute("select * from {};".format(country))
    rows=cur.fetchall()
    t= PrettyTable([ 'Month', 'Confirmed', 'Deceased'])
    for x,y,z in rows:
        t.add_row([x,y,z])
    print(t)
    

def view():                                           #function to view all data in the table
    cur.execute("USE {};".format(cont))
    print("Data for", country , "is : ")
    cur.execute("select * from {};".format(country))
    rows=cur.fetchall()
    t= PrettyTable([ 'Month', 'Confirmed', 'Deceased'])
    for x,y,z in rows:
        t.add_row([x,y,z])
    print(t)
    
    

def viewStat():                                       #function to View data in different formats
    view()
    print('''MENU OPTIONS:
                 1.View the maximum No. of ...
                 2.View the minimum No. of ...
                 3.View the Average No. of ...
                 4.View the data in ascending order
                 5.View the data in descending order
                 6.View totals''')
    try:
        z=int(input("Enter menu option (1-6):"))
    except:
        return
    if z>6:
        return
    if z==1:
        print("Data for", country , "is : ")
        colm=input("Enter column name :")
        cur.execute("select max({}) from {};".format(colm,country))
        t= PrettyTable(['Maximum({})'.format(colm)])
        for x in rows:
            t.add_row([x])
        print(t)



    if z==2:
        print("Data for", country , "is : ")
        colm=input("Enter column name :")
        cur.execute("select min({}) from {}".format(colm,country))
        rows=cur.fetchall()
        t= PrettyTable(['Minimum({})'.format(colm)])
        for x in rows:
            t.add_row([x])
        print(t)
           

    if z==3:
        print("Data for", country , "is : ")
        colm=input("Enter column name :")
        cur.execute("select avg({}) from {};".format(colm,country))
        rows=cur.fetchall()
        t= PrettyTable(['Average {}'.format(colm)])
        for x in rows:
            t.add_row([x])
        print(t)
        
    if z==4:
        print("Data for", country , "is : ")
        colm=input('Enter column name to be ordered by :')
        cur.execute("select * from {} ORDER BY {} ;".format(country,colm))
        rows=cur.fetchall()
        t= PrettyTable([ 'Month', 'Confirmed', 'Deceased'])
        for x,y,z in rows:
            t.add_row([x,y,z])
        print(t)
        

    if z==5:
        print("Data for", country , "is : ")
        colm=input('Enter column name to be ordered by :')
        cur.execute("select * from {} ORDER BY {} DESC ;".format(country,colm))
        rows=cur.fetchall()
        t= PrettyTable([ 'Month', 'Confirmed', 'Deceased'])
        for x,y,z in rows:
            t.add_row([x,y,z])
        print(t)
        

    if z==6:
        print("Data for", country , "is : ")
        cur.execute("select sum(confirmed),sum(deceased) from {};".format(country))
        rows=cur.fetchall()
        t= PrettyTable(['Total confirmed ','Total deceased '])
        for x,y in rows:
            t.add_row([x,y])
        print(t)
        
           
    
def  update():                                        #function to update values in the tables                   
    print('Table before update :') 
    view()
    cur.execute("USE {};".format(cont))
    mth=input("Enter month's record which has to be updated :")
    
    
    try:
        colm=int(input('''Enter column number to be updated
                          1. MONTH      
                          2. CONFIRMED
                          3. DECEASED
                          : '''))
    except:
        return

    if colm>3:
        return
    val=input("Enter new value to be changed: ")
    
    if colm==1:  
        cur.execute("UPDATE {} SET {} ='{}' WHERE {}='{}' ;".format(country,"Month",val,"month",mth))
        print('Update has been completed')
    if colm==2:
       cur.execute("UPDATE {} SET {} ={} WHERE {}='{}';".format(country,"Confirmed",val,'month',mth))
       print('Update has been completed')
    if colm==3:
        cur.execute("UPDATE {} SET {} ={} WHERE {}='{}';".format(country,"Deceased",val,'month',mth))
        print('Update has been completed')
    mydb.commit()
                

def deli():                                           #function to delete values or whole table
    print("***********Delete Sub Menu************")
    print("| 1=> Delete All Record                |")
    print("| 2=> Delete by Month                  |")
    print("| 3=> Exit to Main Menu                |")
    try:
        u=int(input("Enter menu option (1-3):"))
    except:
        return
    if u>3:
        return

    if u==1:  
        pretty()
        rows=cur.fetchall()
        print(rows)
        cur.execute("Delete from {};".format(country))
        mydb.commit()
        print("DATA REMOVED.")

    elif u==2:
        pretty()
        c=input("Enter name of month whose record is to be deleted:")
        cur.execute("delete from {} where month='{}';".format(country,c))
        mydb.commit()
        print("DATA REMOVED.")

    elif u==3:
        return
             
def ins():                                            #function to insert values into tables
    view()
    val1=input("Enter month: ")
    val2=int(input("Enter confirmed cases: "))
    val3=int(input("Enter deaths: "))
    cur.execute("insert into {} values ('{}', {}, {});".format(country,val1,val2,val3))
    mydb.commit()
    view()
      
def menuCountry():                                    #menu for functions
    while True:
        print('''MENU OPTIONS:
                 1.View Country Statistics
                 2.Update Country Statistics
                 3.Delete Country Statistics
                 4.Insert Country Statistics
                 5.View data in different formats
                 6.Main Menu''')

        try:
            z=int(input("Enter menu option (1-6):"))
        except:
            return
        if z>6:
            return

        if z==1:
            view()
        if z==2:
            update()
        if z==3:
            deli()
        if z==4:
            ins()
        if z==5:
            viewStat()
        if z==6:
            return
    
#__main__    
print("Welcome to the Official COVID-19 Pandemic Database")               #MAIN MENU


while True:
    print('''CONTINENTS DATABASES                                                      
             1. ASIA
             2. NORTH AMERICA
             3. SOUTH AMERICA
             4. AFRICA
             5. EUROPE''')

    try:
        x=int(input("Enter menu option of continent (1-5):"))
    except:
        continue


    if x>5:
        continue
    
    #ASIA
    if x==1:     
        print('''Country Statistics
                 1.India
                 2.China
                 3.Malaysia
                 4.Russia
                 5.Sri Lanka''')
        cont= "Asia"

        try:
            y=int(input("Enter menu option of country (1-5):"))
        except:
            continue


        if y>5:
            continue

        if y==1:
            country="India"
        if y==2:
            country="China"
        if y==3:
            country="Malaysia"
        if y==4:
            country="Russia"
        if y==5:
            country="Sri Lanka"
        


    #NA
    if x==2:
        print('''Country Statistics
                 1.USA
                 2.Mexico
                 3.Canada''')
        cont="North_America"
        try:
            y=int(input("Enter menu option of country (1-3):"))
        except:
            continue


        if y>3:
            continue
        if y==1:
            country="USA"
        if y==2:
            country="Mexico"
        if y==3:
            country="Canada"
       
    #SA
    if x==3:
        print('''Country Statistics
                 1.Bolivia
                 2.Brazil
                 3.Chile
                 4.Peru
                 5.Ecuador''')
        cont="South_America"
        try:
            y=int(input("Enter menu option of country (1-5):"))
        except:
            continue


        if y>5:
            continue
        if y==1:
            country="Bolivia"
        if y==2:
            country="Brazil"
        if y==3:
            country="Chile"
        if y==4:
            country="Peru"
        if y==5:
            country="Ecuador"
            
    #AFRICA
    if x==4:
        print('''Country Statistics
                 1.Nigeria
                 2.Ghana
                 3.Mozambique
                 4.Morocco
                 5.Algeria''')
        cont="Africa"
        try:
            y=int(input("Enter menu option of country (1-5):"))
        except:
            continue


        if y>5:
            continue
        if y==1:
            country="Nigeria"
        if y==2:
            country="Ghana"
        if y==3:
            country="Mozambique"
        if y==4:
            country="Morocco"
        if y==5:
            country="Algeria"         
 
    #EUROPE
    if x==5:
        print('''Country Statistics
                 1.Spain
                 2.Italy
                 3.UK
                 4.Norway
                 5.Switzerland''')
        cont="Europe"
        try:
            y=int(input("Enter menu option of country (1-5):"))
        except:
            continue


        if y>5:
            continue
        if y==1:
            country="Spain"
        if y==2:
            country="Italy"
        if y==3:
            country="UK"
        if y==4:
            country="Norway"
        if y==5:
            country="Switzerland"
    cur.execute("USE {};".format(cont))        
    menuCountry()

    
    x=input("Exit? y/n: ")
    if x=='y':
        break
    
#END

