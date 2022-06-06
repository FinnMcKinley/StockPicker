import random
from datetime import date

today = date.today()
dateToday = today.strftime("%d/%m/%y")
counter = 0
nasdaqTable = open('nasdaq_table.txt', 'r')
portfolio = open('portfolio.txt', 'a')
content = nasdaqTable.readlines()

for i in content:
    if i:
        counter += 1

randomNumber = random.randint(2,counter)
randomNumberCorrected = randomNumber + 1

portfolio.write(dateToday)
portfolio.write(" ")
portfolio.write(content[randomNumber][2:7])
portfolio.write(content[randomNumber][98:107])
portfolio.write("\n")
portfolio.close()

print("Today is", dateToday)
print("Today's StockPick is:", content[randomNumber][2:7], content[randomNumber][98:107])
print("Portfolio has been updated.")

nasdaqTable.close()