from . import parse
from math import gcd, modf

# All strictly for IO, return strings, and may not preserve precision

def feetToInches(lenFt):
    return f"{lenFt * 12:g}\""

def inchesToFeet(lenIn):
    return f"{lenIn / 12:g}'"

def numToFrac(num, precision = 16):
    frac = [round(num * precision), precision]
    denom = gcd(frac[0], frac[1])

    frac[0] //= denom
    frac[1] //= denom
    return str(frac[0]) + "/" + str(frac[1])

def numToMixedNum(num, precision = 16):
    decimal, whole = modf(num)
    frac = numToFrac(decimal, precision)
    spacing = " " if (whole != 0) else ""
    return str(int(whole)) + spacing + frac

def inchToMixedMeasurment(num, precision = 16):
    feet = str(int(num // 12))
    inches = numToMixedNum(num % 12)
    return feet + "' " + inches + "\""


# returns a length in decimal inches, for ease
def length(len, type = "in"):
    if (isinstance(len, str)):
        return parse.parseLen(len)
    
    if (type == 'ft'):
        return feetToInches(len)
    elif (type == "mm"):
        return len / 25.4
    elif (type == "cm"):
        return len / 2.54
    elif (type == "m"):
        return len * 39.36
    else:
        return len