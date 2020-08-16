import pymysql

# define connection - name - conn
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

# define function - fAddSubject
def  fAddSubject(nParN,nParT,nParLC):
    # check database connection
    if (not conn):
        # function fConnectDB - call
        fConnectDB() # connect database - school

	# parameter - %s - %s - %s -  nParN - nParT - nParLC
    nInsert="INSERT INTO subject (Name,Teacher,OnLeavingCert) VALUES(%s,%s,%s)"

    # close when finished
    with conn:
        # create object - cursor on connection
        cursor=conn.cursor()
        # execute sql - nQuery
        nCheckUpdate=cursor.execute(nInsert,(nParN,nParT,nParLC))
        print(nCheckUpdate)