lis = [10,1.7782794100389228,1.1547819846894583,1.036632928437698,1.0090350448414476,1.0022511482929128,1.0005623126022085,1.0001405485169472,1.000035135277462]

def finaltermtoadd(x):
    if x == 1:
        return 0
    arr = x
    x = x - 1
    y = x/(1+x) + (x*x)/2
    return y*0.4342944819

z = float(input('Enter number :'))
copyofz = z
if 1 > z:
    z = 1/z

answeradder = 0
counter = 1
for number in lis:
    if z == 1:
        break
    while True:
        if z >= number:
            z = z/number
            answeradder = answeradder + 1/counter
        if number > z:
            counter = counter*4
            break

answeradder = answeradder + finaltermtoadd(z)
if 1 > copyofz:
    answeradder = -answeradder

print(f"The log to the base 10 of {copyofz} is {answeradder}.")