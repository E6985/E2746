# define function - main
def main():
	# function fPromptEnterName - call
	nNameStr=fPromptEnterName()
	# function fPromptEnterAge - call
	nAgeStr=fPromptEnterAge()
	while True: # infinite
		# function fDisplayMenu - call
		fDisplayMenu()
		nChoice=input("Choice: ")
		if (nChoice=="3"):
			break # exit
		elif (nChoice=="1"):
			# function fGetName - call
			nName=fGetName(nNameStr)
			print(nName.upper())
		elif (nChoice=="2"):
			try:
				# function fGetAge - call
				nAge=fGetAge(nAgeStr)
				print(nAge+1)
			except:
				print("> Invalid Age Entered")

# define function - fDisplayMenu
def fDisplayMenu():
	print("")
	print("MENU")
	print("====")
	print("1 - Get Name")
	print("2 - Get Age")
	print("3 - Exit")

# define function - fPromptEnterName
def fPromptEnterName():
	return "Enter Name: "

# define function - fPromptEnterAge
def fPromptEnterAge():
	return "Enter Age: "

# define function - fGetName
def fGetName(nParName):
	return input(nParName)

# define function - fGetAge
def fGetAge(nParAge):
	return int(input(nParAge))

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function __main__ - call
    main()