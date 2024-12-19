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

inVal = "-1039" # input('Enter a float: ')
inFloat = float(inVal)
print(inFloat)

intPart = abs(int(inFloat))
print(intPart)

fracPart = inFloat - intPart;

intStr = f'{intPart:b}'
# Integer part in binary (string)
print("Binary integer part: " +  intStr)

# fraction par in binary
fractStr = fractToBin(fracPart)

print("Binary fractional part: " + fractStr)


fullBin =  intStr + fractStr
onePos = fullBin.find('1')
pointPos = len(intStr) - onePos - 1
print(f"One place: {onePos}, shift: {pointPos}")

exponent = 15 + pointPos;
print(f"Exponent: {exponent}")

signStr = '0'
exponentStr = f'{exponent:05b}'  # Limit to 5 bits
mantissa = fullBin[1:]
mantissa = mantissa[0:10]  # limit the mantissa to 10 bits

if (inFloat < 0):
    signStr= '1'


print("Result: " + signStr + ' ' + exponentStr + ' ' + mantissa)




