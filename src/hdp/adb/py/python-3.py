# define function - main
def main():
	nArray=[]
	# function fDisplayMenu - call
	fDisplayMenu()
	while True: # infinite
		nChoice=input("Enter choice: ")
		if (nChoice=="1"):
			# function fFillArray - call
			nArray=fFillArray()
			# function fDisplayMenu - call
			fDisplayMenu()
		elif (nChoice=="2"):
			print(nArray)
			# function fDisplayMenu - call
			fDisplayMenu()
		elif (nChoice=="3"):
			# function fDisplayMenu - call
			fDisplayMenu()
			# function fFindGtInArray - call
			fFindGtInArray(nArray)
		elif (nChoice=="4"):
			break; # exit
		else:
			# function fDisplayMenu - call
			fDisplayMenu()

# define function - fDisplayMenu
def fDisplayMenu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")

# define function - fFillArray
def fFillArray():
    nLocArray=[]
    while True: # infinite
        nLocX=int(input("Enter Number(s): "))
        if (nLocX==-1):
        	break # exit
        nLocArray.append(nLocX)
    return nLocArray

# define function - fFindGtInArray
def fFindGtInArray(nParArray):
	nLocArrayGT=[]
	nLocGT=int(input("Enter Number: "))
	for nEachValue in nParArray:
		if (nEachValue>nLocGT):
			nLocArrayGT.append(nEachValue)
	print(nLocArrayGT)

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function __main__ - call
    main()