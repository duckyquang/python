# This is the long, broken one that my dumb brain didn't think through

import math

def getUserInput():
    print("The format should be ax^2+bx+c=0")
    
    RIGHTINPUT = False
    
    while RIGHTINPUT == False:
        userInput = input("What's your equation: ")
        if userInput == "STOP":
            print("Stopped.")
            break        
        elif userInput[-1] != "0":
            print("Wrong format.")
            continue
        elif not "x" in userInput:
            print("Please use the right variable!")
            continue
        elif not "x^2" in userInput:
            print("Where's your x squared (x^2)!?")
            continue
        elif userInput.count("x") < 2:
            print("Still missing bx!")
            continue
        else:
            userInput = userInput.replace(" ", "")
            return userInput
            RIGHTINPUT = True

def breakdownEquation(equation):
    XSQUAREDINDEX = equation.index("x^2")
    A = int(equation[:XSQUAREDINDEX]) if XSQUAREDINDEX > 0 else int(equation[XSQUAREDINDEX])
    
    XINDEX = equation.find("x", XSQUAREDINDEX + 1, len(equation))
    index = XSQUAREDINDEX + 3
    
    for i in range(index, XINDEX):
        B += equation[index]
        index += 1
    
    if B[0] == "+":
        B = B.replace("+", "")
    
    EQUALSIGNINDEX = equation.find("=")
    index = equation.find(B) + len(B) + 1
    
    for i in range(index, EQUALSIGNINDEX):
        C += equation[index]
        index += 1
    
    if C[0] == "+":
        C = C.replace("+", "")
    
    A = int(A)
    B = int(B)
    C = int(C)
    
    return A, B, C
        
def calcEquation(a, b, c):
    
    XREAL = None
    
    if b*b - 4*a*c > 0:
        X_1 = (-b + math.sqrt(b*b - 4 * a * c)) / 2 * a
        X_2 = (-b - math.sqrt(b*b - 4 * a * c)) / 2 * a
    
        print(f"\nThe first X is: {X_1}")
        print(f"The second x is: {X_2}")
        
        XREAL = True
    elif b*b - 4*a*c == 0:
        X = (-b + math.sqrt(b*b - 4 * a * c)) / 2 * a
    
        print(f"\nThe only X is: {X}")
        XREAL = True
    elif b*b - 4*a*c < 0:
        print(f"\nThere are no real x.")
        XREAL = False
        
    if XREAL == True:
        VALIDINPUT = False
        
        while VALIDINPUT == False:
            userInput = input("Do you want to round the number? (y or n): ")
            
            if userInput == "y":
                VALIDINPUT == True
                
                ROUNDINPUTVALID = False
                
                while ROUNDINPUTVALID == False:
                    roundNum = input("To how many decimal points: ")
                    
                    if roundNum.isnumeric() == True:
                        ROUNDINPUTVALID = True
                        X_1 = math.round(X_1, roundNum)
                        X_2 = math.round(X_2, roundNum)
                    
                        print(f"\nThe rounded first X is: {X_1}")
                        print(f"The rounded second x is: {X_2}")
                    else:
                        print("Wrong input!")
                        continue
                
                break
            elif userInput == "n":
                VALIDINPUT == True
                print("Thanks for using the calculator!")
                break
            else:
                print("Wrong input!")
                continue

def main():
    userInput = getUserInput()
    a, b, c = breakdownEquation(userInput)
    calcEquation(a, b, c)

if __name__ == "__main__":
    print(breakdownEquation("x^2+2x+15=0"))
