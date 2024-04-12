# @author Orrin Monroe
# This program allows a user to process daily high temperatures from a file
# in a satandard format.

import sys

def main():
    # Create an empty list named dailyHighs and months
    dailyHighs = []
    months = []

    # Call getDailyHighs with "2021DailyHighsKCMO.csv" and the dailyHighs list.
    # To test a different file, 2021DailyHighsKCMO-Partial.csv may also be used.
    getDailyHighs("2021DailyHighsKCMO.csv",months,dailyHighs)       
    EXIT = "5"
    choice = "0"
    
    # Present user with menu choices until they decide to exit
    while (choice != EXIT):

        choice = getMenuChoice()
        print()
        
        # Process each menu choice
        if (choice == "1"): 
            # See the description/requirements document for the code to insert
            # to get the value for monthIndex
            monthIndex = -1
            while monthIndex < 0:
                month = input("Month? ")
                try:
                    monthIndex = months.index(month)
                except:
                    print(f"{month} not recognized")
                    
            # Call getAverageHigh and display the returned average to 1 digit
            # of precision followed by F. Precede this with a header
            # of "Average High: ". See the sample runs.
            avgHigh = getAverageHigh(monthIndex, dailyHighs)
            print(f"Average High: {avgHigh}:.")+"F"
            
        elif (choice == "2"):
            print("Show temperatures within what range? ")
            low = int(input("Lower bound: "))
            high = int(input("Upper bound: "))
            # Insert a call to showTempsInRange
            showTempInRange(low,high,dailyHighs,months)
            
        elif (choice == "3"):
            overUnder = int(input("Over/Under temperature? "))
            # Insert code to get the tuple returned from a call to getOverUnder.
            # Then, display the tuple data in the format shown
            
            
        elif (choice == "4"):
            filename = input("Name of file to create? ")
            
            # If the filename does not end with .html or .htm then concatenate
            # (apppend) .html to the file name. Hint: use the endsWith method
            # to determine if it ends with .html or .htm
            # Then, insert a call to createWebPage Stats with the filename
        
        print()

# getMenuChoice presents and menu and gets the user's choice
# @return The user's choice
def getMenuChoice():
    print("(1) Show average daily high for a given month.")
    print("(2) Show daily high temperatures within a given range.")
    print("(3) Show over/under statistics for a given temperature.")
    print("(4) Store statistics as Web page.")
    print("(5) Exit.")
    return input(f"Choice? ")

# getDailyHighs reads temperature data from a file in a specified format.
# Each line (record) consists of the month name followed by the highs for
# each day in the month. All fields in the record are comma-separated.
# @param filename The name of the file from which temperatures are read
# @param months An empty list to be filled with months
# @param dailyHighs An empty list that will become a two-dimensonal list.
#                   Each row will hold a list of temperatures for a month.
def getDailyHighs(filename,months,dailyHighs):
    import csv
    list  = []
    
    try:
        with open (filename) as inFile:
            reader = csv.reader(inFile, delimiter = ',')
            for line in reader:
                    months.append(line[0])
                    for i in line[1:]:
                        list.append(int(i))
            for f in list:
                dailyHighs.append(list[f])
    except Exception as exc:
        print(f"{exc} Application exit.")
    finally:
        if ("inFile" in locals()):
            inFile.close()   
    
# getAverageHigh determines the average daily high for a given month
# @param monthIndex The index of the given month
# @param dailyHighs A two-dimensional list of annual temperatures
# @return The average daily high
def getAverageHigh(monthIndex, dailyHighs): 
    return sum(dailyHighs[monthIndex]) / len(dailyHighs[monthIndex])
    

# showTempInRange shows temperatures lying within a given range in
# a table format.
# @param lowerBound The inclusive lower bound for the temperatures
# @param upperBound The inclusive upper bound for the temperatures
# @param dailyHighs A two-dimensional list of annual temperatures
# @param months A list containing the months.
def showTempInRange(lowerBound,upperBound,dailyHighs,months):
    print(f"Day")
    for i in range(1,31):
        print(f"{i}")
    print()
    for i in range(len(months)):
        print(months[i])
        if (dailyHighs[i] >= lowerBound and dailyHighs[i] <= upperBound):
            print(f"{dailyHighs[i]}")
        else:
            print('*')

# getOverUnder counts the number of temperatures below, equal to, and
# above a given temperature
# @param overUnder The over/under value that splits the counts
# @param dailyHighs A two-dimensional list of annual temperatures

# createWebpageStats stores each month with its lowest high and highest high
# to a Web page file
# @param filename The name of the file
# @param dailyHighs A two-dimensional list of annual temperatures
# @param months A list containing the months.  
#def createWebPageStats(filename, months, dailyHighs):
    ROW_COLORS = ("lightsteelblue", "beige") # Use different colors if desired.
    PAGE_BEGIN = '<html>\n' + \
        '<head>\n' + \
        '    <meta charset="utf-8">\n' + \
        '    <title>2021 Temperatures</title>\n' + \
        '</head>\n' + \
        '<body>\n' + \
        '<table style = "border-spacing:1px;">\n' + \
        '  <tr style = "background-color:lightgray">\n' + \
        '    <td>Month</td>\n' + \
        '    <td>Lowest Daily High</td>\n' + \
        '    <td>Highest Daily High</td>\n' + \
        '  </tr>\n'
    
    # Insert code to open filename for writing, and then write PAGE_BEGIN to
    # that file
    
    # Insert one loop that processes one month (one row in the html table)
    # each iteration. See the discussion in the description/requirements doc

    # Insert code to write PAGE_END to file. Then, close the file and display
    # to the user that the file was created. You will need to output the name
    # of the file when mathching the output.
    PAGE_END = '</table>\n</body>\n</html>'
    
main()