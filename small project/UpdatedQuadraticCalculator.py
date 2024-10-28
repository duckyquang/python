# The good quadratic calculator

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

def read(equation):
    XSQUAREDINDEX = equation.index("x^2")
    
    if equation[0] == "x": A = "1"
    elif equation[:2] == "-x": A = "-1"
    else: A = equation[:XSQUAREDINDEX]
    
    XINDEX = equation.index("x", XSQUAREDINDEX + 1, len(equation))
    
    if equation[XSQUAREDINDEX+3:XINDEX] == "-": B = "-1"
    elif equation[XSQUAREDINDEX+3:XINDEX] == "+": B = "1"
    else: B = equation[XSQUAREDINDEX+3:XINDEX]
    
    EQUALSIGNINDEX = equation.index("=")
    
    if equation[XSQUAREDINDEX+3:XINDEX] == "-" or equation[XSQUAREDINDEX+3:XINDEX] == "+":
        C = equation[XINDEX + len(B):EQUALSIGNINDEX]
    else:
        C = equation[XINDEX + len(B) - 1:EQUALSIGNINDEX]
    
    if C[0] == "+":
        C = C.replace("+", "")
    
    A = int(A)
    B = int(B)
    C = int(C)
    
    return A, B, C

def calculateEquation(a,b,c):
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
    a, b, c = read(userInput)
    discriminant = b*b - 4*a*c
    
    print(f"\na: {a}, b: {b}, c: {c}")
    print(f"Discriminant: {discriminant}")
    calculateEquation(a,b,c)

if __name__ == "__main__":
    main()
