#make a fuction that takes an argument of a string of a basic math formula with 
#one operation
def basicCalculator(string):
    firstnum = True
    num1 = ''
    num2 = ''
    for ch in string:
        if not ch.isdigit():
            operate = ch
            firstnum = False
        elif firstnum:
            num1 += ch
        elif not firstnum and ch.isdigit():
            num2 += ch
    num1 = int(num1)
    num2 = int(num2)
    
    if operate == '+':
        return num1 + num2
    elif operate == '-':
        return num1 - num2
    elif operate == '/':
        return num1 / num2
    elif operate == '*':
        return num1 * num2

running = True
while running:
    inp = "Enter a one operation math problem with no spaces.\n"
    enter =  "If you would like to end the program, enter 'q'. \nEnter problem here: "
    question = input(inp+enter)
    if question == 'q':
        running = False
        break
    else:
        ans = basicCalculator(question)
        print(f"Yor answer: {round(ans, 3)}")
        print('\n')
        print()