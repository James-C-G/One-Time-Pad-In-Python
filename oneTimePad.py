def encrypt(fileData, fileKey):
    outPut = ""
    keyArray = list(fileKey)
    j = 0
    append = ""
    for i in fileData:
        if i.isalpha() == False:
            outPut += i
            continue

        if i.islower():
            lower = True
        else:
            lower = False
        i = i.lower()
        
        offSet = (ord(i) + ord(keyArray[j]))
        
        if offSet > 218:
            offSet -= 122
            append = chr(offSet)
            
        if offSet > ord("z"):
            while offSet > ord("z"):
                offSet -= 96
            append = chr(offSet)
        else:
            append = chr(offSet)

        if lower:
            outPut += append
        else:
            outPut += append.upper()
        
        j+= 1

        if j == len(keyArray):
            j = 0
            
    return outPut                        
    
def decrypt(fileData, fileKey):
    outPut = ""
    keyArray = list(fileKey)
    j = 0
    append = ""
    for i in fileData:
        if i.isalpha() == False:
            outPut += i
            continue

        if i.islower():
            lower = True
        else:
            lower = False
        i = i.lower()
        
        offSet = (ord(i) - ord(keyArray[j]))

        if offSet < 1:
            offSet += 122
            append = chr(offSet)    
        
        if offSet < ord("a"):
            while offSet < ord("a"):
                offSet += 96
            append = chr(offSet)
        else:
            append = chr(offSet)

        if lower:
            outPut += append
        else:
            outPut += append.upper()
        
        j+= 1

        if j == len(keyArray):
            j = 0
            
    return outPut 

def writeOutput(outPut):
    try:
        txtFile = open(fileName,"w")
        try:
            txtFile.write(outPut)
        finally:
            txtFile.close()
            print(outPut)
    except FileNotFoundError:
        print("File no longer exists")

def getKey():
    while True:
        inpString = input("Please input a key: ")
        if inpString.isalpha():
            return inpString

def getProcessType():
    while True:
        processType = input("Would you like to Encrypt(e) or Decrypt(d)? ")
        if processType == "d":
            return processType
        elif processType == "e":
            return processType
        print("Plese put a valid input")

def getTxtFile():
    while True:
        global fileName
        fileName = input("Please input a file name: ")
        try:
            txtFile = open(fileName,"r")
            try:
                txtInFile = txtFile.read()
                return txtInFile
            finally:
                txtFile.close()
        except FileNotFoundError:
            print("That file doesn't exist ")

def getChoice():
    while True:
        usrInp = input("Would you like to keep going? (Yes/No) ")
        if usrInp == "no" or usrInp == "No":
            return 0
        elif usrInp == "yes" or usrInp == "Yes":
            return 1
        print("Input something valid")
        
def main():
    running = True
    while running:
        processType = getProcessType()
        fileData = getTxtFile()
        fileKey = getKey()
        if processType == "e":
            writeOutput(encrypt(fileData, fileKey))
        else:
            writeOutput(decrypt(fileData, fileKey))
        choice = getChoice()
        if choice == 0:
            running = False
    print("Exiting...")
    
if __name__ == "__main__":
    main()
