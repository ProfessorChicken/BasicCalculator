quIt = False
step = 0
stored_value = 0
while not quIt:
    if step == 0:
        print("This calculator program can perform the operations +, -, *, **, /, //, and %. To use the previous result in your calculation, substitute "
                "\"ans\" for that number")

    and1 = input("Operand 1: ")
    tor = input("Operator: ")
    and2 = input("Operand 2: ")

    if (and1 == "ans"):
        and1 = stored_value
    elif (and2 == "ans"):
        and2 = stored_value

    and1 = float(and1)
    and2 = float(and2)

    if (tor == "+"):
        answer = and1 + and2
    elif (tor == "-"):
        answer = and1 - and2
    elif (tor == "*"):
        answer = and1 * and2
    elif (tor == "/"):
        answer = and1 / and2
    elif (tor == "//"):
        answer = and1 // and2
    elif (tor == "%"):
        answer = and1 % and2
    elif (tor == "**"):
        answer = and1 ** and2

    print("the answer is " + str(answer))
    stored_value = answer
    step += 1
