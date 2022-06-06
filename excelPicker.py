import random
from datetime import date
from openpyxl import Workbook

today = date.today()
dateToday = today.strftime("%d/%m/%y")
randomNumber = random.randint(0,750)
print(randomNumber)
print(dateToday)
