from Utils.units import length
from Utils import units
  

def printToggles():
    for i in range(1, 9):
        height = 24 * i
        print(str(units.inchesToFeet(height)) + ': ' + units.inchToMixedMeasurment(getLen(height)))

def getLen(height):
    innerHeight = height - length(' 1/8" ')
    sf = innerHeight / length(''' 15' 10 1/2" ''')
    return (sf * 23.75) + 22.5