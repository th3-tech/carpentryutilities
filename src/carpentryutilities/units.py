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
    if (frac == "1/1"):
        frac = "0"
        whole += 1

    wholeStr = "" if (whole == 0) else str(int(whole))
    spacing = "" if (whole == 0 or frac[0] == '0') else " "
    fracStr = "" if (frac[0] == '0') else frac
    return wholeStr + spacing + fracStr

def inchesToMixedMeasurment(lenIn, precision = 16):
    feet = str(int(lenIn // 12)) + "'" if (lenIn >= 12) else ""
    inches = numToMixedNum(lenIn % 12, precision)
    inches = "" if (inches == "") else " " + inches + "\""
    return feet + inches

# returns a length in decimal inches, for ease
def length(len, type = "in"):
    if (isinstance(len, str)):
        return parse.parseLen(len)
    
    if (type == 'ft'):
        return len * 12
    elif (type == "mm"):
        return len / 25.4
    elif (type == "cm"):
        return len / 2.54
    elif (type == "m"):
        return len * 39.36
    else:
        return len