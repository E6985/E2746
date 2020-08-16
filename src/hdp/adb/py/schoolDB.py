import pymysql

conn=None

# define function - fConnectDB
def fConnectDB():
    # accessible any function
    global conn
    conn=pymysql.connect(
    	host="localhost",
    	user="root",
    	password="yu3s74mt",
    	db="school",
    	cursorclass=pymysql.cursors.DictCursor)

# define function - fGetExperience
def fGetExperience(nParN):
    # check database connection
    if (not conn):
        # function fConnectDB - call
        fConnectDB() # connect database - school
	
    # parameter - nParN - %s
    nQuery="SELECT * FROM teacher WHERE experience<%s"

    with conn:
        # create object - cursor
        cursor=conn.cursor()
        # execute sql - nQuery - pass parameter - nParN
        cursor.execute(nQuery,(nParN))
        # return - cursor - all rows 
        nResult=cursor.fetchall()
        # return - caller function  
        return nResult