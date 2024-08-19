import random 

#list of operators to choose from
OP = ["+", "-", "*"]

#minimum and maximum values for the operands
MIN_OP = 3
MAX_OP = 12

def generate_problem():
    #generate a random integer between MIN_OP and MAX_OP for the left/right operand
    left = random.randint(MIN_OP, MAX_OP)
    right = random.randint(MIN_OP, MAX_OP)
    
    #select an operator from the OP list
    operator = random.choice(OP)

    #convert left and right operands to strings for concatenation with the operator
    #the str() function is used here to convert the integer operands into strings
    #this allows us to concatenate them with the operator (which is already a string)
    expr = str(left) + " " + operator + " " + str(right)
    
    #ealuate the answer
    answer = eval(expr)
    
    #return expression & the calculated answer
    return expr, answer


#the function generate_problem() returns two values: 
# 1.the generated expression (as a string)
# 2.the evaluated answer (as a number)
#these values are unpacked and assigned to expr and answer respectively.
#the order here is important: expr stores the expression, and answer stores the result.
expr, answer = generate_problem()

#print(expr, answer)

TotalProblems = 10


for i in range(TotalProblems):
    expr, answer = generate_problem()
    while True:
        gess_answer = input("Problem " + str(i + 1) + " " + expr + " : ")
        if gess_answer == str(answer) :
            print(" Great Job !🫣" )
            break
        else: 
            print("please try again your answer is not correct 😓")