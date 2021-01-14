import re

print("Calculator")
print("Type <exit> to exit\n\n")

previous = 0
run = True

def doMaths():
    global run
    global previous
    calculation = ""
    
    if previous == 0:
        calculation = input("Enter calculation: ")
    else:
        calculation = input(str(previous))

    if calculation == "exit":
        run = False
    else:
        calculation = re.sub('[A-Za-z,.:()" "]', '', calculation) # this removes everything but numbers and mathematical operators, as python commands can be run through eval
        
        if previous == 0:
            previous = eval(calculation) # performs the calculation stored in the variable
        else:
            previous = eval(str(previous) + calculation) # allows a continuous calculation

while run:
    doMaths()