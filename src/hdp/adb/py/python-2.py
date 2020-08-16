# define function - main
def main():
    nListPrime=[2,3,5,7]
    nListEmpty=[]
    for nEachValue in nListPrime:
        # function fDoubleNumber - call
        nListEmpty.append(fDoubleNumber(nEachValue))
    print(nListEmpty)

# define function - fDoubleNumber
def fDoubleNumber(nParNumber):
    return nParNumber*2

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function __main__ - call
    main()