## testing
import numpy as np
from datetime import datetime
from calendar import monthrange

theta = np.array([9,  10,  11,  12,  13,  14,  15,  16,  33,  34,  35,  36,  37,  38,  39,  40,  57,  58,  59,  60,  61,  62,  63,  64,  81,  82,  83,  84,  85,  86,  87,  88, 120, 121, 122, 123, 124, 125, 126, 127,])

datetime_end = datetime(year=2023, month=9, day=4,hour=12,minute=0)
max_days = monthrange(datetime_end.year, datetime_end.month)
dayby_hr = datetime_end.weekday() * 24
hrof_end = dayby_hr + datetime_end.hour

for i in range(len(theta)):
    if hrof_end in theta:
        print("No shift required.")
        noshift = True
        new_th = 0
        break
    elif hrof_end > theta[i]:
        noshift = False
        new_th = 0
        pass
    elif hrof_end < theta[i]:
        noshift = False
        new_th = theta[i]
        break

if new_th == 0:  # over the week
    new_th = theta[0] + 168

if noshift == False:
    theta_day = int(np.floor(new_th / 24))
    new_day = (theta_day - datetime_end.weekday() + datetime_end.day)
    if new_day > max_days[1]:  ## rolling over to the next month
        theta_month = int(np.floor(new_day) / max_days[1])
        new_month = theta_month + datetime_end.month
        new_day -= max_days[1]
    else:
        new_month = datetime_end.month
    if new_month > 12:  ## rolling over to the next year
        theta_year = int(np.floor(new_month) / 12)
        new_year = theta_year + datetime_end.year
        new_month -= 12
    else:
        new_year = datetime_end.year    
    new_hour = new_th - theta_day * 24
    new_datetime = datetime(year=new_year,month=new_month,day=new_day,hour=new_hour,minute=0)

if noshift == True:
    new_datetime = np.copy(datetime_end)
    
print(datetime_end)
print(new_datetime)