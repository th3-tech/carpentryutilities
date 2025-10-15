def parseFrac(frac):
    fracClean = frac.strip()
    parts = fracClean.split("/")
    decimal = int(parts[0]) / int(parts[1])
    return decimal

def parseLen(term):
    term = term.strip()

    feet = 0
    whole = 0
    frac = 0

    if (not "'" in term):
        feet = 0
        inches = term
    elif(not "\"" in term):
        inches = 0
        feet = float(term.strip("' "))
    else:
        feet, inches = term.split("'")
        feet = float(feet.strip())

    if ("\"" in term):
        inches = inches.strip("\" ")
        if (" " in inches):
            whole, fracStr = inches.split(" ", 1)
            whole = float(whole.strip())
            frac = parseFrac(fracStr)
        elif ("/" in inches):
            frac = parseFrac(inches)
        else:
            whole = float(inches)
    
    totalLen = feet * 12 + whole + frac

    return totalLen


