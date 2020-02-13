#Make a program that accepts binary/decimal numbers and converts to other form
def binToDec(string):
    '''take string of a binary number and convert it to decimal'''
    #length = length of the binary string
    length = len(string)
    #create the variable num to track the final number
    num = 0
    #calculate the num by iterating from the back of the list to the front
    for i in range(0, length):
        #place is = to the length of string - 1 - i to iterate in reverse order
        place = length - 1 - i
        #if the number is a 1 calculate and add it's value to num
        if string[place] == '1':
            calc = 2 ** i
            num += calc
    return num

def decToBin(string):
    '''take string of a decimal number and convert it to decimal'''
    #turn string into number
    string = int(string)
    #num is the string to return at the end of the function
    num = ''
    #determine the length the binary string will be
    #x is the base value of 2^i
    x = 0
    #e keeps track of how long the binary string will need to be to hold the decimal
    e = 0
    #whike x is smaller than the number being evaluated
    while x < string:
        #x = 2^e
        x = 2 ** e
        #if x is larger than number being evaluated
        if x > string:
            #break from while loop
            break
        #otherwise... add one to e and evaluate again
        e += 1
    #iterate from 0 to e+1 (first z is zero so e - 0 is e)
    for z in range(0, e+1):
        # eval is e - z.. so starting from the largest base going to the smallest
        eval = e - z
        #cal is that base's place value
        cal = 2 ** eval
        #if cal is smaller than string...
        if cal < string:
            #string is now = to string - cal
            string -= cal
            # add a 1 to num string
            num += '1'
        #if cal > than string
        else:
            #dont operate and add zero to num string
            num += '0'
    return num 
