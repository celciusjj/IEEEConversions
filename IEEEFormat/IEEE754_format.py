import math
import numpy as np
from utils import convertEntero, convertDecimal, getBinaryIntPart, getBinaryDecimalPart

"""Function to convert a number to IEEE 754 format"""
def convertToIEEE(num, base):
    integerPart = getBinaryIntPart(round(math.modf(abs(num))[1]))
    decimalPart = getBinaryDecimalPart(
        math.modf(abs(num))[0], len(integerPart) - 1, base)
    exponent = len(integerPart) - 1 + (127 if base == 32 else 1023)
    exponentBinary = getBinaryIntPart(exponent)
    return str("1" if num < 0 else "0") + exponentBinary + integerPart[1:] + decimalPart


"""This function gets the exponent given the number and a bool variable
    to verify if it is a 32 bit number or not"""
def getExponentialNumber(number, is32bit):
    arrayNumber = []
    counter = 0
    if(is32bit):
        exponentialBin = number[1:9]
        for numero in exponentialBin[::-1]:
            arrayNumber.append((2**counter) * int(numero))
            counter = counter+1
        return (np.sum(arrayNumber) - 127)
    else:
        exponentialBin = number[1:12]
        for numero in exponentialBin[::-1]:
            arrayNumber.append((2**counter) * int(numero))
            counter = counter+1
        return (np.sum(arrayNumber) - 1023)


"""This function calculates the mantise given a number, the exponenet,
    and a bool variable to verify if it is a 32 bit number or not"""
def calculateMantisa(number, exponentialNumber, is32bit):
    if(is32bit):
        mantisa = number[9:32]
        newMantisa = mantisa[:exponentialNumber] + \
            ',' + mantisa[exponentialNumber:]
        finalMantisa = "1"+newMantisa
        return finalMantisa
    else:
        mantisa = number[12:64]
        newMantisa = mantisa[:exponentialNumber] + \
            ',' + mantisa[exponentialNumber:]
        finalMantisa = "1"+newMantisa
        return finalMantisa


"""Given a binary number it converts that number to its decimal form"""
def convertToDecimal(number, base):
    is32Bits = True if base == 32 else False
    counter = 0
    numbersToConvert = []
    exponential = getExponentialNumber(number, is32Bits)
    finalMantisa = calculateMantisa(number, exponential, is32Bits)
    numbersToConvert = finalMantisa.split(",")
    finalNumber = float(convertEntero(
        numbersToConvert[0]) + convertDecimal(numbersToConvert[1]))
    return finalNumber * -1 if number[0] == "1" else finalNumber
