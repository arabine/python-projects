import math
import struct


def convBinToDec(inVal):
    #print("Entrez un nombre binaire")
    size = len(inVal)
    powMax = 2**(size-1);

    print("NB digits: " + str(size))
    print("Puissance max: " + str(powMax))

    decVal = 0

    for d in inVal:
        decVal += int(d) *  powMax
        powMax /= 2
        #print(d)
        
    print(inVal + " in decimal is: " + str(int(decVal)))

def convDecToBin(inVal):
    binVal = ""
    decVal = int(inVal);
    while decVal > 0:
        if (decVal % 2) == 0:
            binVal = '0' + binVal
        else:
            binVal = '1' + binVal
        decVal = int(decVal / 2);
    return str(binVal)


def convHexToDec(inVal):

    size = len(inVal)
    powMax = 16**(size-1);
    
    print("NB digits: " + str(size))
    print("Puissance max: " + str(powMax))
    
    decVal = 0
    for d in inVal:
        digitVal = 0
        asciiNum = ord(d)
        if (asciiNum >= 65):
            digitVal = 10 + (asciiNum - ord("A"))
        else:
            digitVal = asciiNum - ord("0")
        
        decVal += powMax * digitVal
        powMax /= 16
        
    print(str(int(decVal)))


def convDecToHex(inVal):
    decVal = int(inVal);
    hexVal = "";
    while decVal > 0:
        
        divPart = (decVal % 16);
        
     #   print(divPart)
        digit = ""
        if divPart > 9:
            digit = chr(ord("A") + (divPart - 10))
        else:
            digit = str(divPart)

        hexVal = digit + hexVal
        decVal = int(decVal / 16)
    
    return str(hexVal)


#input('Enter a float: ')
convBinToDec("1100110010001100")
print(convDecToBin("52364"))


convHexToDec("CC8C") # "CC8C"
print(convDecToHex("52364"))


