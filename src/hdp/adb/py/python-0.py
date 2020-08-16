# define function - main
def main():
	nName=input("Enter Name: ")
	# try - nAge - convert to integer
	try:
		# int - string to integer
		nAge=int(input("Enter Age: "))
	# except - try block exception 
	except:
		print("Invalid Age")
		# program end
		return
	if (nAge<18):
		print("Too Young")
	else:
		nNewAge=nAge+2
		print(nName+"@somecompany.ie",nNewAge)

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function main - call
    main()