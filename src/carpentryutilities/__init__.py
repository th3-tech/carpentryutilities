from . import parse, units
# SPDX-FileCopyrightText: 2025-present th3-tech <83879091+th3-tech@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

# Function Aliases
fti = units.feetToInches
pfti = lambda a : print(units.feetToInches(a))
itf = units.inchesToFeet
pitf = lambda a : print(units.inchesToFeet(a))
itmm = units.inchesToMixedMeasurment
pitmm = lambda a : print(units.inchesToMixedMeasurment(a))
pf = pitmm
len = units.length