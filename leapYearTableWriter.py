# Definitions
YEAR_REGISTER_LENGTH = 7
IS_LEAPYEAR_FILENAME = "myIsLeapyear.txt"

MAX_ELEMENTS_IN_FILELINE = 8 # required logisim format
# Script code

# Open file and initialize

leapYearFile = open(IS_LEAPYEAR_FILENAME, "w")
leapYearFile.write("v2.0 raw\n")
elementsInLineCount = 0 # for ensuring logisim format

# Leap year algorithm implementation
for table_entry in range(2**14):
        year = table_entry % 128 + (table_entry // 128) * 100
        # divisable by 4
        if year % 4 == 0:
                if year % 100 == 0:
                # divisable by 100
                        if year % 400 == 0:
                        # divisible by 400
                                isLeapYear = 1
                        else:
                        # not divisible by 400
                                isLeapYear = 0
                else:
                # not divisible by 100
                        isLeapYear = 1
        else:
        # not divisible by 4
                isLeapYear = 0

        elementsInLineCount = elementsInLineCount + 1
        if elementsInLineCount == MAX_ELEMENTS_IN_FILELINE:
                leapYearFile.write(str(isLeapYear) + "\n")
                elementsInLineCount = 0
        else:
                leapYearFile.write(str(isLeapYear) + " ")

leapYearFile.close()
