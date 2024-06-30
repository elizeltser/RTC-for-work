#Definitions
REGISTER_LENGTH = 7
TABLE_FILENAME = "7bitToBCDTable.txt"

MAX_ELEMENTS_IN_FILELINE = 8 # required logisim format
# Script code

# Open file and initialize

bitToBCDTable = open(TABLE_FILENAME, "w")
bitToBCDTable.write("v2.0 raw\n")

elementsInLineCount = 0 # for ensuring logisim format

# 7bitToBCD translation 

for num in range(2 ** REGISTER_LENGTH):

    elementsInLineCount = elementsInLineCount + 1
    if elementsInLineCount == MAX_ELEMENTS_IN_FILELINE:
        bitToBCDTable.write(str(min(num, 99)) + "\n")
        elementsInLineCount = 0
    else:
        bitToBCDTable.write(str(min(num, 99)) + " ")

bitToBCDTable.close()
