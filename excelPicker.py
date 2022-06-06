import random
from datetime import date

today = date.today()
dateToday = today.strftime("%d/%m/%y")
randomNumber = random.randint(0,750)
print(randomNumber)
print(dateToday)
