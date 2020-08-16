import  pymysql
import schoolUpdateDB

# define function - main
def main():
	nName=input("Enter Subject:  ")
	nTeacher=input("Enter Teacher: ")
	nLOC=input("Enter on Leaving Cert <1/0>: ")

	try:
		# function schoolUpdateDB.fAddSubject - call
		schoolUpdateDB.fAddSubject(nName,nTeacher,nLOC)
	except pymysql.err.IntegrityError as nE:
		print("Subject Already Exists -",nE)
	# catch all errors
	except Exception as nE:
		print("Generic ERROR",nE)

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function main - call
    main()