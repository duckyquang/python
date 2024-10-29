import math

def main():
    STOP = False
    calculations = 0
    
    while STOP == False:
        if calculations == 0:
            print("Welcome to the calculator.")
        
        calculations += 1
        
        userInput = input("What's your equation: ")
        userInput = userInput.replace(" ","")
        
        if userInput.count("x") == 0: print("No x found."); continue
        elif userInput.count("x") < 2: print("Missing bx."); continue
        
        if "x^2" in userInput:
            XSQUAREDINDEX = userInput.index("x^2")
            if userInput[0] == "x": A = "1"
            elif userInput[:2] == "-x": A = "-1"
            else: A = userInput[:XSQUAREDINDEX]
        else:
            print("No x^2 found.")
            continue
        
        XINDEX = userInput.index("x", XSQUAREDINDEX+1, len(userInput))
        
        if userInput[XSQUAREDINDEX+3:XINDEX] == "-": B = "-1"
        elif userInput[XSQUAREDINDEX+3:XINDEX] == "+": B = "1"
        else: B = userInput[XSQUAREDINDEX+3:XINDEX]
        
        if "=0" in userInput:
            EQUALSIGNINDEX = userInput.index("=")
            if userInput[XSQUAREDINDEX+3:XINDEX] == "-" or userInput[XSQUAREDINDEX+3:XINDEX] == "+": C = userInput[XINDEX + len(B):EQUALSIGNINDEX]
            else: C = userInput[XINDEX + len(B) - 1:EQUALSIGNINDEX]
        else: print("The equation must be equal to zero."); continue
        
        if int(B)*int(B) - 4*int(A)*int(C) > 0:
            X_1 = (-int(B) + math.sqrt(int(B) * int(B) - 4 * int(A) * int(C))) / 2 * int(A)
            X_2 = (-int(B) - math.sqrt(int(B) * int(B) - 4 * int(A) * int(C))) / 2 * int(A)
            print(f"\nThe first X is: {X_1}")
            print(f"The second x is: {X_2}")
        elif int(B)*int(B) - 4*int(A)*int(C) == 0:
            X = (-int(B) + math.sqrt(int(B) * int(B) - 4 * int(A) * int(C))) / 2 * int(A)
            print(f"\nThe only X is: {X}")
        elif int(B)*int(B) - 4*int(A)*int(C) < 0: print(f"\nThere are no real x."); continue
        
        VALIDINPUT = False
        
        while VALIDINPUT == False:
            userInput = input(f"\nDo you want to round the number? (y or n): ")
            if userInput == "y":
                VALIDINPUT = True
                ROUNDINPUTVALID = False
                while ROUNDINPUTVALID == False:
                    roundNum = input("To how many decimal points: ")
                    if roundNum.isnumeric() == True:
                        ROUNDINPUTVALID = True
                        print(f"\nThe rounded first X is: {round(X_1, int(roundNum))}")
                        print(f"The rounded second x is: {round(X_2, int(roundNum))}")
                    else: print("Wrong input!"); continue
            elif userInput == "n": VALIDINPUT = True
            else: print("Wrong input!"); continue
        
        INPUT = False
        
        while INPUT == False:       
            userStopDecision = input(f"\nDo you want to continue (y or n): ")
            if userStopDecision == "y": INPUT = True
            elif userStopDecision == "n": INPUT = True; STOP = True
            else: print("Wrong input.")

if __name__ == "__main__":
    main()
