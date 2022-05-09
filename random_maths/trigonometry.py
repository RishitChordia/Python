def tangent(inputnumber):
    number = 1001
    pi = 3.141592653589793238462643383279
    inputnumber = inputnumber*pi/180
    inputsquare = inputnumber*inputnumber
    denominator = number
    while True:
        number = number - 2
        denominator = number - inputsquare/(denominator)
        if number == 1:
            break
    denominator = inputnumber/denominator
    return denominator

def squareroot(secxsquare):
    secxsquarecopy = secxsquare
    secx = 1
    previoussecx = 0
    while True:
        previoussecx = secx
        secx = (secx + secxsquarecopy/secx)/2
        if secx == previoussecx:
            return secx

inputnumber = float(input('Enter θ between 0 and 45 degree :'))
if inputnumber >= 360:
    while True:
        inputnumber = inputnumber - 360
        if inputnumber >= 0 and inputnumber < 360:
            break

if inputnumber < 0:
    while True:
        inputnumber = inputnumber + 360
        if inputnumber >= 0:
            break
        

operation = int(input('Enter 1 to find sinθ, 2 to find cosθ, 3 to find tanθ, 4 to find cosecθ, 5 to find secθ and 6 to find cotθ :'))
tanx = tangent(inputnumber)
secsquarex = 1 + tanx*tanx
secx = squareroot(secsquarex)
if operation == 1:
    final = tanx/secx
    print(final)
if operation == 2:
    final = 1/secx
    print(final)
if operation == 3:
    final = tanx
    print(final)
if operation == 4:
    final = secx/tanx
    print(final)
if operation == 5:
    final = secx
    print(final)
if operation == 6:
    final = 1/tanx
    print(final)