def raisedto(numbb,index):
    numbbcopy = numbb
    while True:
        if index == 1:
            return numbb
            break
        if index == 0:
            return 1
            break
        numbb = numbb*numbbcopy
        index = index - 1

def assumption(someinput,logcounterforh):
    root = 1
    tempopempo = 1
    rootcopy = root
    counter = 1
    while True:
        rootcopy = root
        tempopempo = (tempopempo*someinput)/counter
        root = root + tempopempo
        counter = counter + 1
        # if counter > logcounterforh:
        #     return root
        #     break
        if rootcopy == root:
            return root
            break

whichroot = int(input('Which root do you want :'))
inputnumber = float(input('Enter number :'))


def roooots(inputnumber,whichroot):
    if inputnumber == 1:
        return 1
    counterforh = 1
    h = 0
    while True:
        if inputnumber >= counterforh and inputnumber < counterforh*10:
            break
        else:
            counterforh = counterforh*3.1622776601683793319988935444327
            h = h+0.5

    temp1 = h + 5
    h = 2*(h*2.3025850929940456840179914546844)/whichroot
    # print(h)
    
    copies = whichroot - 1
        
    # root = 1 + h + (h*h)/2 + (h*h*h)/6 + (h*h*h*h)/24 + (h*h*h*h*h)/120 + (h*h*h*h*h*h)/720
    root = assumption(h,temp1)
    counter = 0
    rootcopy = 1
    temp1 = 1
    # print(root)
    while True:
        temp1 = raisedto(root,copies)
        rootcopy = root
        root = ((root*copies) + (inputnumber/temp1))/whichroot
        counter = counter + 1
        if root == rootcopy:
            # print(counter)
            return root 

print(roooots(inputnumber,whichroot))
