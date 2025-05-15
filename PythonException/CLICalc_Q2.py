

#--------------------------------------------------------------------------
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
#--------------------------------------------------------------------------
def multiply(a, b):
    return a * b
#--------------------------------------------------------------------------
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b



#-----------------------------------Main Function---------------------------------------
def calc():
    try:
        expression = input("Enter the expression in one line seperated by spaces : \n") 
        expr = expression.strip().split()
        # print(expr)
        if len(expr) < 3 or len(expr) % 2 == 0:
            print("Invalid Expresion Format")
            return
        ops_map = {
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide
        }
        result = float(expr[0])

        for i in range(1, len(expr),2):
            operator = expr[i]
            num = float(expr[i+1])
            if operator not in ops_map:
                print("Invalid Operator : ",operator)
                return
            
            result = ops_map[operator](result,num)
        print(expression," = ",result)
    except ZeroDivisionError as e:
        print("Error : ",e)
        


#------------------------------Man function-------------------------------------------------
calc()

# sample : 
# Input: 10 + 2 - 4 * 3 / 2
# Input: 1.5 + 2.5 * 2

