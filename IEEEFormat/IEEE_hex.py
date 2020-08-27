import math
import numpy as np
from utils import getLetterFromNum, getHexIntPart, getHexDecimalPart, getNumFromLetter, calculateMantisaHex, getExponentialNumberHex

"""Given a number it returns the equivalent to the IEEE hex format"""
def getIEEEHexNum(num):
    intPart = getHexIntPart(round(math.modf(abs(num))[1]))
    decimalPart = getHexDecimalPart(math.modf(abs(num))[0])
    exponent = "0" + getLetterFromNum(len(intPart))
    bothNumbers = intPart + decimalPart  # Add both numbers
    bothNumbers = bothNumbers[:8]
    mantise = (bothNumbers).ljust(8 - len(intPart) -
                                  len(decimalPart) + len(bothNumbers), "0")
    return str("1" if num < 0 else "0") + exponent + mantise


"""Given a IEEE hex number it returns its decimal form"""
def calculateBaseTen(number):
    counter = 0
    numbersToConvertEntera = []
    numbersToConvertDecimal = []

    for numero in calculateMantisaHex(number, getExponentialNumberHex(number))[0][::-1]:
        numbersToConvertEntera.append(
            (16**counter) * int(getNumFromLetter(numero)))
        counter = counter+1

    counter = -1
    for numero in calculateMantisaHex(number, getExponentialNumberHex(number))[1]:
        numbersToConvertDecimal.append(
            (16**counter) * int(getNumFromLetter(numero)))
        counter = counter-1
    result = np.sum(numbersToConvertEntera) + np.sum(numbersToConvertDecimal)
    return result * -1 if number[0] == "1" else result
