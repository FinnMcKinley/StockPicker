import random
from datetime import date
from openpyxl import load_workbook

today = date.today()
dateToday = today.strftime("%d/%m/%y")
randomNumber = random.randint(0,750)
print(randomNumber)
print(dateToday)

wb = load_workbook(filename= 'ExcelSheet.xlsx')
ws = wb.active
print(ws['A1'].value)
