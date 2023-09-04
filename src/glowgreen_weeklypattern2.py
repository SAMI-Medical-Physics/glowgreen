from glowgreen import ContactPatternRepeating, Clearance_1m
from datetime import datetime
import calendar
import numpy as np

### test weekly matches daily
# theta_week = [9,33,57,81,105,129,153]
# c_week     = [8,8,8,8,8,8,8]
# d_week     = [0.5,0.5,0.5,0.5,0.5,0.5,0.5]

### bug case to test
theta_week = [9,33,57,81,120]
c_week     = [8,8,8,8,8]
d_week     = [0.5,0.5,0.5,0.5,0.5]

### test rollover
# theta_week   = [0,72,148]
# c_week       = [24,24,20]
# d_week       = [0.3] * 3

cpat_week = ContactPatternRepeating(theta_week, c_week, d_week, repeat="week")

# cpat_week.plot()

admin_datetime = datetime(year=2021, month=12, day=30,hour=23,minute=0)
# theta_shift = cpat_week._shift_weekly_pattern(admin_datetime)

# exp clearance
# dose_rate_init_1m = 100# uSv/h
# effective_half_life = 10 # h
# cfit = Clearance_1m(
    # "exponential", [dose_rate_init_1m, effective_half_life], 1.0)

# biexp clearance
dose_rate_init_1m = 50  # uSv/h
fraction1 = 0.3
half_life1 = 40 # h
half_life2 = 40 # h
cfit = Clearance_1m(
    "biexponential", [dose_rate_init_1m, fraction1, half_life1, half_life2], 1.0)

dose_constraint = 1  # mSv
restriction_period, dose, datetime_end = cpat_week.get_restriction(cfit, dose_constraint,admin_datetime)
assert dose <= dose_constraint

print("Length of restriction period: ", restriction_period, "hrs")
print("Dose to caregiver:            ", dose, "mGy")
print("Start of restriction period:  ", calendar.day_name[admin_datetime.weekday()], admin_datetime)
print("End of restriction period:    ", calendar.day_name[datetime_end.weekday()], datetime_end)

cpat_week.plot(cfit=cfit, dose_constraint=dose_constraint, admin_datetime=admin_datetime)