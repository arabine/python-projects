import math
import struct

exp_len = 5
mant_len = 10
bias = 15

def fractToBin(fract):
    fractStr = ''
    for x in range(10):
        fract = fract * 2

        intPart = int(fract)
        fract = fract - intPart;
        fractStr += '' + str(intPart)

    return fractStr

def binToFloat(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

inVal = "34.5" # input('Enter a float: ')
inFloat = float(inVal)
print(inFloat)

intPart = int(inFloat)
print(intPart)

fracPart = inFloat - intPart;

# fracPart = 0
# if "." in inVal:
#     fracPart = int(str(inFloat).split('.')[-1])

print(fracPart)

intStr = f'{intPart:b}'
# Integer part in binary (string)
print("Binary integer part: " +  intStr)

# fraction par in binary
fractStr = fractToBin(fracPart)

print("Binary fractional part: " + fractStr)

pointPos = len(intStr)
print("Decimal point position: " + str(pointPos))

fullBin =  intStr + fractStr
onePos = fullBin.find('1')
print("One place: " + str(onePos))

if pointPos > onePos:
    pointPos -= 1

exponent = 15 + pointPos;

signStr = '0'
exponentStr = f'{exponent:05b}'  # Limit to 5 bits
mantissa = fullBin[1:]
mantissa = mantissa[0:10]  # limit the mantissa to 10 bits

if (inFloat < 0):
    signStr= '1'


print("Result: " + signStr + ' ' + exponentStr + ' ' + mantissa)




