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
        print "During the month of" ,months[i], "you spent" ,monthExpenses[i]
    return


    

def prediction(calculatedNum, studentIncome):
    adjustedIncome =(abs(calculatedNum) + studentIncome + 300)
    print "in order to live comfortably next semester you will need " ,adjustedIncome, "."
    return

def outputExpenses(finalExpenses):
    if finalExpenses > 0 and finalExpenses != 0:
        print "Your current fall semester balance is" ,finalExpenses
    elif finalExpenses != 0 and finalExpenses < 0:
        print "You are in debt with" ,finalExpenses, "Dollars"
        print "Watch this video for help on managing your finances: https://www.youtube.com/watch?v=mXYyEjRfO18"
    elif finalExpenses == 0:
        print "You are broke with" ,finalExpenses, "Dollars."
        print "Watch this video for help on managing your finances: https://www.youtube.com/watch?v=mXYyEjRfO18"
    return

monthExpenses = []
global calculatedNum
calculatedNum = 0
months = ['August', 'September', 'October', 'November', 'December']
categories = ['Food', 'Rent', 'Bills', 'Other']
studentIncome = input("What is your income for the fall semester?")
global finalExpenses
finalExpenses = 0




inputExpenses(monthExpenses, months, categories)
for i in monthExpenses[:]:
    calculatedNum += int(i)
    finalExpenses = (studentIncome - calculatedNum)
outputExpenses(finalExpenses)
prediction(calculatedNum, studentIncome)









