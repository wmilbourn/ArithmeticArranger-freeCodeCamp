def arithmetic_arranger(problems, solve = False):

    arranged_problems=[]

    if len(problems) > 5: #limiting the number of problems to five 
        return "Error: Too many problems." 
    #establishing variables for each line in the final display
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i, problem in enumerate(problems): #loops through each problem within the original list
        items = problem.split(" ")
        first = items[0]
        second = items[2]
        operator = items[1]
        
        if len(first) > 4 or len(second) > 4: #limiting number length
            return "Error: Numbers cannot be more than four digits."
        
        if first.isdigit() == False or second.isdigit() == False: #numbers only
            return "Error: Numbers must only contain digits."
        
        if not(operator == "+" or operator == "-"): #+ or - only
            return "Error: Operator must be '+' or '-'."

        longest = len(max(items, key=len)) #length of the longest number
        middleSpace = longest - len(second) + 1 #calculates number of spaces on the middle line
        middle = operator + (middleSpace * ' ') + second #operator and the second number with appropriate spacing
        top = first.rjust(len(middle)) #first number justified to the right
        dash = ''
        for lines in middle: #creating how long the line should be
            dash += '-'
        
        if operator == "+": #addition
            solution = int(first) + int(second)
        else: #subtraction
            solution = int(first) - int(second) 
#formatting requires all top numbers to be added to one line, etc.
        line1 += top.rjust(longest)
        line2 += middle.rjust(longest)
        line3 += dash
        line4 += str(solution).rjust(len(middle))
#four spaces between the problems, none after the last one
        if i < len(problems)-1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    arranged_problems = line1 + "\n" + line2 + "\n" + line3 

    if solve == True:
        arranged_problems += "\n" + line4

    return arranged_problems
