num = 123123456

if num == 0:
    print("Zero")
    
nums = str(num)
divided = []
extra = len(nums) % 3

if extra != 0:
    divided.append(nums[0:extra])

for i in range(int(str(len(nums) / 3)[0])):
    divided.append(nums[i * 3 + extra : (i + 1) * 3 + extra])

divided.reverse()

ones = ["Zero ", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
tens = ["Zero ", "Ten ", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
teens = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
suffixes = ["Thousand ", "Million ", "Billion ", ""]

outcome = []
temporaryOutcome = ""

if extra == 0:
    domain = 3
else:
    domain = extra

for x in range(len(divided)):
    for y in range(domain if x == len(divided) - 1 else 3):
        if int(divided[x][y]) == 0:
            continue
        elif int(divided[x][y]) == 1 and y == 1 and len(divided[x]) == 3:
            temporaryOutcome += teens[int(divided[x][2])]
            break
        elif int(divided[x][y]) == 1 and y == 0 and len(divided[x]) == 2:
            temporaryOutcome += teens[int(divided[x][1])]
            break
        elif y == 0 and len(divided[x]) == 3:
            temporaryOutcome += ones[int(divided[x][y])] + "Hundred "
        elif y == 1 and len(divided[x]) == 3:
            temporaryOutcome += tens[int(divided[x][y])]
        elif y == 0 and len(divided[x]) == 2:
            temporaryOutcome += tens[int(divided[x][y])]
        else:
            temporaryOutcome += ones[int(divided[x][y])]
    
    outcome.append(temporaryOutcome)
    temporaryOutcome = ""

outcome.reverse()
divided.reverse()
actualOutcome = ""

for i in range(len(outcome)):
    if len(outcome) > 1:
        if divided[i] != '000':
            actualOutcome += outcome[i] + suffixes[len(outcome) - 2 - i]
    else:
        actualOutcome += outcome[i]

print(actualOutcome[:-1])
