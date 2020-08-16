import schoolDB

# define function - main
def main():
	while True: # infinite
		# db - send actual number
		try:
			# function fGetNumber - call
		    nNumber=int(fGetNumber())
			# function schoolDB.fGetExperience - call
		    nTeachers=schoolDB.fGetExperience(nNumber)
		    for nEachRow in nTeachers:
		    	# db - rows - columns - tid - Name - level - experience - dob
		    	print(nEachRow["tid"],"|",
		    		nEachRow["Name"],"|",
		    		nEachRow["level"],"|",
		    		nEachRow["experience"],"|",
		    		nEachRow["dob"] )
		    break # - valid nNumber - exit
		# not actual number - iterate
		except Exception as nE:
			print("Invalid Number - Try Again")

# define function - fGetNumber
def fGetNumber():
    return input("Enter Number: ")

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function main - call
    main()