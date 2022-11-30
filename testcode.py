def arithmetic_arranger(problems, solver = False):

    finalAnswer=[]

    if len(problems) >= 5: #limiting the number of problems to five
        return "Error: Too many problems"
        
    for x in problems:
        numbers = x.split(" ")
        first = int(numbers[0])
        second = int(numbers[2])
        operator = numbers[1]

        if len(first) > 4 or len(second) > 4: # number length parameter
            return "Error: Numbers cannot be more than four digits."

        if first.isdigit() == False & second.isdigit() == False: # numbers only parameter
            return "Error: Numbers must only contain digits."

        if operator != "+" or operator != "-": # + or - only parameter
            return "Error: Operator must be '+' or '-'."

        biggest = len(max(numbers, key=len)) # biggest of the two numbers
        spaces = biggest - len(second) + 1 # number of spaces in the second line
        middle = operator + (spaces*' ') + second # operator and second number
        top = first.rjust(len(middle)) # first number, justified to the right
        line = ''
        for y in middle: # creating how long the line should be
            line =+ '-'           

        if operator == "+": # calculating addition
            solution = int(first) + int(second)
        elif operator == "-": # calculating subtraction
            solution = int(first) - int(second)
            
        answer = str(solution).rjust(len(middle))
        if solver == True: 
            sets = str(top) + '\n' + str(middle) + '\n' + str(line) + '\n' + str(answer)
            finalAnswer.append(sets)
        else:    
            sets = str(top) + '\n' + str(middle) + '\n' + str(line)
            finalAnswer.append(sets)
        
    return('     '.join(finalAnswer)) 


    
    


arithmetic_arranger(["5 + 14","112 + 2","85 - 3", "4 + 64", "2 - 1"], True)

                        #format the numbers to the correct output display
#                        probWidth = len(max(numbers, key=len))
                        # print(numbers.rjust(probWidth))
  #                      myProblem = ' '
  #                      for y in numbers:
   #                         myProblem += ' '+ y
   #                     output = myProblem.rjust(probWidth)
    #                    print(output)                          