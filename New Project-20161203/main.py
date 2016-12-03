import webbrowser
def inputExpenses(monthExpenses, months, categories):
    "This gets the expenses of the semenster"
    num = 0
    for i in months[:]:
        for j in categories[:]:
            num += float(raw_input("During the month of %s how much did you spend on %s" %(i,j)))
        monthExpenses.append(num)
        num = 0
    "Prints out the total cost of the semester"
    for i in range(0, len(months)):
        print "During the month of" , months[i] , "you spent", monthExpenses[i]
        file.write("During the month of" 'months[i]'  "you spent" 'monthExpenses[i]')
    return

def prediction(calculatedNum, studentIncome, file):
    if finalExpenses <= 99:
        adjustedIncome =(abs(calculatedNum) + abs(finalExpenses) + 300)
        print "In order to live comfortably next semester you will need " ,adjustedIncome, "."
        file.write("In order to live comfortably next semester you will need " 'adjustedIncome' ".")
    elif finalExpenses >= 100:
        print "You are living comfortably at this rate! Keep up the great finance management"
        file.write("You are living comfortably at this rate! Keep up the great finance management")
    return

def outputExpenses(finalExpenses, file):
    if finalExpenses > 0 and finalExpenses != 0:
        print "Your current fall semester balance is" ,finalExpenses
        file.write("Your current fall semester balance is" 'finalExpenses')
    elif finalExpenses != 0 and finalExpenses < 0:
        print "You are in debt with" ,finalExpenses, "Dollars"
        webbrowser.open("https://www.youtube.com/embed/mXYyEjRfO18")
        print "Watch this video for help on managing your finances: https://www.youtube.com/watch?v=mXYyEjRfO18"
        file.write("You are in debt with" 'finalExpenses' "Dollars")
    elif finalExpenses == 0:
        print "You are broke with" ,finalExpenses, "Dollars."
        print "Watch this video for help on managing your finances: https://www.youtube.com/watch?v=mXYyEjRfO18"
        webbrowser.open("https://www.youtube.com/embed/mXYyEjRfO18")
        file.write("You are broke with" 'finalExpenses' "Dollars.")
    return

file = open("Finances", 'w')
monthExpenses = []
global calculatedNum
calculatedNum = 0
months = ['August', 'September', 'October', 'November', 'December']
categories = ['Food', 'Rent', 'Bills', 'Other']
studentIncome = input("What is your income for the fall semester?")
file.write('studenIncome')
global finalExpenses
finalExpenses = 0

inputExpenses(monthExpenses, months, categories)
for i in monthExpenses[:]:
    calculatedNum += int(i)
    finalExpenses = (studentIncome - calculatedNum)
print "You spent $" , calculatedNum, "for this semester."
file.write("You spent $" 'calculatedNum' "for this semester.")
outputExpenses(finalExpenses,file)
prediction(calculatedNum, studentIncome, file)
file.close()
