import math
import numpy as np

"""Given a binary number it returns its integer decimal form"""
def convertEntero(number):
    counter = 0
    NumberPreDec = []
    for numero in number[::-1]:
        NumberPreDec.append((2**counter) * int(numero))
        counter = counter+1
    return (np.sum(NumberPreDec))


"""Given a decimal binary dumber it returns its decimal form"""
def convertDecimal(number):
    counter = -1
    NumberPostDec = []
    for numero in number:
        NumberPostDec.append((2**counter) * int(numero))
        counter = counter-1
    return round((np.sum(NumberPostDec)), 2)


"""This function parses a integer number from decimal to binary"""
def getBinaryIntPart(num):
    finalString = ""
    while num != 1 and num != 0:
        finalString = finalString + str(num % 2)
        num = math.trunc(num / 2)
    return str(finalString + str(num))[::-1]


"""This function parses a decimal number from decimal to binary"""
def getBinaryDecimalPart(num, integerLenght, base):
    finalString = ""
    while num != 1 and num != 0:
        mult = num * 2
        finalString = finalString + str("1" if mult >= 1 else "0")
        num = mult if mult < 1 else mult - 1
    mantise = 23 if base == 32 else 52
    return finalString[0:mantise - integerLenght] if len(finalString) >= mantise else finalString.ljust(mantise - integerLenght, "0")


"""Given a number it returns its equivalent to hex form"""
def getLetterFromNum(num):
    num = int(num)
    if num <= 9:
        return str(num)
    elif num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num == 13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"
    else:
        return str(num)


"""Given an integer number it returns the equivalent to the hex form"""
def getHexIntPart(num):
    finalString = ""
    while num != 1 and num != 0:
        finalString = finalString + getLetterFromNum(str(num % 16))
        num = math.trunc(num / 16)
    return str(num) + str(finalString)[::-1] if num == 1 else str(finalString)[::-1]


"""Given a decimal number it returns the equivalente to the hex form"""
def getHexDecimalPart(num):
    finalString = ""
    while num != 1 and num != 0:
        mult = num * 16
        roundedNumber = round(math.modf(abs(mult))[1])
        finalString = finalString + getLetterFromNum(roundedNumber)
        num = mult if mult < 1 else mult - roundedNumber
    return finalString


"""Given a hex number it returns it equivalent to the decimal form"""
def getNumFromLetter(num):
    if num == "A":
        return "10"
    elif num == "B":
        return "11"
    elif num == "C":
        return "12"
    elif num == "D":
        return "13"
    elif num == "E":
        return "14"
    elif num == "F":
        return "15"
    else:
        return str(num)


"""Gets the exponent of a IEEE hex number"""
def getExponentialNumberHex(number):
    arrayNumber = []
    counter = 0
    exponentialBin = number[1:3]
    for numero in exponentialBin[::-1]:
        arrayNumber.append((16**counter) * int(getNumFromLetter(numero)))
        counter = counter+1
    return (np.sum(arrayNumber))


"""Calculates the mantise of a IEEE hex number"""
def calculateMantisaHex(number, exponentialNumber):
    mantisa = number[3:11]
    newMantisa = mantisa[:exponentialNumber] + \
        "," + mantisa[exponentialNumber:]
    return newMantisa.split(",")
