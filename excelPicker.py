import random
from datetime import date
from openpyxl import load_workbook
from openpyxl import Workbook

today = date.today()
dateToday = today.strftime("%d/%m/%y")
randomNumber = random.randint(2,749)
print(randomNumber)
print(dateToday)
randomCell = 'A' + str(randomNumber)
print('randomCell is:')
print(randomCell)

InfoWB = load_workbook(filename= 'ExcelSheet.xlsx')
InfoWS = InfoWB.active

dbWB = load_workbook(filename= 'StockPicks.xlsx')
db = dbWB.active
dbWB.save('StockPicks.xlsx')
