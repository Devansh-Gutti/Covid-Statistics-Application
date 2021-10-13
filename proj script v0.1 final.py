#A complete program script to create a databases for project corona 
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor=mydb.cursor()
def Asia():

    mycursor.execute("CREATE DATABASE IF NOT EXISTS ASIA ;")
    mycursor.execute("USE ASIA ;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS INDIA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS CHINA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS MALAYSIA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS RUSSIA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS SRILANKA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    
def Europe():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS EUROPE ;")
    mycursor.execute("USE EUROPE ;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS SPAIN(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS ITALY(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS UK(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS NORWAY(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS SWITZERLAND(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    

def Africa() :
   mycursor.execute("CREATE DATABASE IF NOT EXISTS AFRICA ;")
   mycursor.execute("USE AFRICA ;")
   mycursor.execute("CREATE TABLE IF NOT EXISTS NIGERIA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
   mycursor.execute("CREATE TABLE IF NOT EXISTS GHANA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
   mycursor.execute("CREATE TABLE IF NOT EXISTS MOZAMBIQUE(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
   mycursor.execute("CREATE TABLE IF NOT EXISTS MOROCCO(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
   mycursor.execute("CREATE TABLE IF NOT EXISTS ALGERIA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    
def NA():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS NORTH_AMERICA ;")
    mycursor.execute("USE NORTH_AMERICA ;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS USA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS MEXICO(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS CANADA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")

def SA():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS SOUTH_AMERICA ;")
    mycursor.execute("USE SOUTH_AMERICA ;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS BOLIVIA(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS BRAZIL(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS CHILE(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS PERU(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS ECUADOR(MONTH CHAR(10), CONFIRMED INTEGER(10), DECEASED INTEGER(10), PRIMARY KEY(MONTH));")

def AsiaD():
    mycursor.execute("USE ASIA ;")
    #INDIA
    mycursor.execute("INSERT INTO INDIA VALUES('March',1394,35);")
    mycursor.execute("INSERT INTO INDIA VALUES('April',33469,1119);")
    mycursor.execute("INSERT INTO INDIA VALUES('May',155946,4254);")
    mycursor.execute("INSERT INTO INDIA VALUES('June',395183,12008);")
    mycursor.execute("INSERT INTO INDIA VALUES('July',1053558,17938);")
    #CHINA
    mycursor.execute("INSERT INTO CHINA VALUES('March',1730,435);")
    mycursor.execute("INSERT INTO CHINA VALUES('April',1528,1319);")
    mycursor.execute("INSERT INTO CHINA VALUES('May',12641,1);")
    mycursor.execute("INSERT INTO CHINA VALUES('June',514,0);")
    mycursor.execute("INSERT INTO CHINA VALUES('July',758,0);")
    
    #RUSSIA
    mycursor.execute("INSERT INTO RUSSIA VALUES('March',1834,17);")
    mycursor.execute("INSERT INTO RUSSIA VALUES('April',104662,1056);")
    mycursor.execute("INSERT INTO RUSSIA VALUES('May',299345,3637);")
    mycursor.execute("INSERT INTO RUSSIA VALUES('June',242009,4627);")
    mycursor.execute("INSERT INTO RUSSIA VALUES('July',192132,4643);")

def EuropeD():
    mycursor.execute("USE EUROPE ;")
    #SPAIN
    mycursor.execute("INSERT INTO SPAIN VALUES('March',171912,9729);")
    mycursor.execute("INSERT INTO SPAIN VALUES('April',68166,16665);")
    mycursor.execute("INSERT INTO SPAIN VALUES('May',14921,3613);")
    mycursor.execute("INSERT INTO SPAIN VALUES('June',10378,335 );")
    mycursor.execute("INSERT INTO SPAIN VALUES('July',55137,91 );")
    #ITALY
    mycursor.execute("INSERT INTO ITALY VALUES('March',104648,12437);")
    mycursor.execute("INSERT INTO ITALY VALUES('April',99673,15570);")
    mycursor.execute("INSERT INTO ITALY VALUES('May',27551,5472);")
    mycursor.execute("INSERT INTO ITALY VALUES('June',7599,1413);")
    mycursor.execute("INSERT INTO ITALY VALUES('July',6978,374);")
    #UK
    mycursor.execute("INSERT INTO UK VALUES('March',22769,2425);")
    mycursor.execute("INSERT INTO UK VALUES('April',132359,24189);")
    mycursor.execute("INSERT INTO UK VALUES('May',93774,10821);")
    mycursor.execute("INSERT INTO UK VALUES('June',34328,2956);")
    mycursor.execute("INSERT INTO UK VALUES('July',19928,798);")

def AfricaD():
    mycursor.execute("USE AFRICA ;")
    #NIGERIA
    mycursor.execute("INSERT INTO NIGERIA VALUES('March',134,2);")
    mycursor.execute("INSERT INTO NIGERIA VALUES('April',1797,56);")
    mycursor.execute("INSERT INTO NIGERIA VALUES('May',8230,231);")
    mycursor.execute("INSERT INTO NIGERIA VALUES('June',15532,303);")
    mycursor.execute("INSERT INTO NIGERIA VALUES('July',17457,288);")
    #GHANA
    mycursor.execute("INSERT INTO GHANA VALUES('March',161,5);")
    mycursor.execute("INSERT INTO GHANA VALUES('April',1913,12);")
    mycursor.execute("INSERT INTO GHANA VALUES('May',5807,19);")
    mycursor.execute("INSERT INTO GHANA VALUES('June',9860,4);")
    mycursor.execute("INSERT INTO GHANA VALUES('July',17760,70);")
    #MOZAMBIQUE
    mycursor.execute("INSERT INTO MOZAMBIQUE VALUES('March',8,0);")
    mycursor.execute("INSERT INTO MOZAMBIQUE VALUES('April',68,0);")
    mycursor.execute("INSERT INTO MOZAMBIQUE VALUES('May',178,2);")
    mycursor.execute("INSERT INTO MOZAMBIQUE VALUES('June',635,4);")
    mycursor.execute("INSERT INTO MOZAMBIQUE VALUES('July',975,5);")
def NAD():
    mycursor.execute("USE NORTH_AMERICA;")
    #USA
    mycursor.execute("INSERT INTO USA VALUES('March',199326,5215);")
    mycursor.execute("INSERT INTO USA VALUES('April',919013,60183);")
    mycursor.execute("INSERT INTO USA VALUES('May',759173,44017);")
    mycursor.execute("INSERT INTO USA VALUES('June',886307,21416);")
    mycursor.execute("INSERT INTO USA VALUES('July',1947871,26992);")
    #MEXICO
    mycursor.execute("INSERT INTO MEXICO VALUES('March',1124,20);")
    mycursor.execute("INSERT INTO MEXICO VALUES('April',17247,1756);")
    mycursor.execute("INSERT INTO MEXICO VALUES('May',71973,8314);")
    mycursor.execute("INSERT INTO MEXICO VALUES('June',137459,17914);")
    mycursor.execute("INSERT INTO MEXICO VALUES('July',201864,19501);")
    #CANADA
    mycursor.execute("INSERT INTO CANADA VALUES('March',8592,89);")
    mycursor.execute("INSERT INTO CANADA VALUES('April',44624,3095);")
    mycursor.execute("INSERT INTO CANADA VALUES('May',37711,4111);")
    mycursor.execute("INSERT INTO CANADA VALUES('June',13257,1296);")
    mycursor.execute("INSERT INTO CANADA VALUES('July',12108,344);")
def SAD():
    mycursor.execute("USE SOUTH_AMERICA;")
    #BOLIVIA
    mycursor.execute("INSERT INTO BOLIVIA VALUES('March',107,8);")
    mycursor.execute("INSERT INTO BOLIVIA VALUES('April',1003,66);")
    mycursor.execute("INSERT INTO BOLIVIA VALUES('May',8482,308);")
    mycursor.execute("INSERT INTO BOLIVIA VALUES('June',22533,997);")
    mycursor.execute("INSERT INTO BOLIVIA VALUES('July',43109,2353);")
    #BRAZIL
    mycursor.execute("INSERT INTO BRAZIL VALUES('March',5715,201);")
    mycursor.execute("INSERT INTO BRAZIL VALUES('April',79665,5700);")
    mycursor.execute("INSERT INTO BRAZIL VALUES('May',429469,23413);")
    mycursor.execute("INSERT INTO BRAZIL VALUES('June',893636,30342);")
    mycursor.execute("INSERT INTO BRAZIL VALUES('July',1257813,32912);")
    #CHILE
    mycursor.execute("INSERT INTO CHILE VALUES('March',3205,35);")
    mycursor.execute("INSERT INTO CHILE VALUES('April',15550,242);")
    mycursor.execute("INSERT INTO CHILE VALUES('May',92281,937);")
    mycursor.execute("INSERT INTO CHILE VALUES('June',168411,5244);")
    mycursor.execute("INSERT INTO CHILE VALUES('July',76292,2941);")
        
    
def drop():
    mycursor.execute("DROP DATABASE IF EXISTS Asia;")
    mycursor.execute("DROP DATABASE IF EXISTS Europe;")
    mycursor.execute("DROP DATABASE IF EXISTS Africa ;")
    mycursor.execute("DROP DATABASE IF EXISTS North_America ;")
    mycursor.execute("DROP DATABASE IF EXISTS South_America;")
    
    
    
    
    
    
    
    
    
    
    

    

#__MAIN__
drop()
Asia()
Europe()
Africa()
NA()
SA()
EuropeD()
AfricaD()
NAD()


        

mydb.commit()
mydb.close()
