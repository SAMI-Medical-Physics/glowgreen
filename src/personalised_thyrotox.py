from glowgreen import ContactPatternRepeating

theta = [7.5, 16]  # Start times (h) of pattern elements
c = [0.75, 3.5]  # Durations (h) of pattern elements
d = [0.3, 1]  # Distances (m) of pattern elements
cpat = ContactPatternRepeating(theta, c, d)

cpat.plot()

from glowgreen import Clearance_1m

a0 = 555  # MBq
dose_rate_init_1m = 0.05 * a0  # uSv/h
distance = 1  # m
fraction1 = 0.73
half_life1 = 6.7  # h
half_life2 = 139  # h

cfit = Clearance_1m(
    "biexponential", [dose_rate_init_1m, fraction1, half_life1, half_life2], distance
)

from datetime import datetime, timedelta

dose_constraint = 1  # mSv
admin_datetime = datetime(day=4, month=8, year=2022, hour=14, minute=0)
restriction_period, dose, datetime_end = cpat.get_restriction(
    cfit, dose_constraint, admin_datetime
)

assert dose <= dose_constraint
assert datetime_end == admin_datetime + timedelta(hours=restriction_period)

print(restriction_period, dose, datetime_end)

cpat.plot(cfit=cfit, dose_constraint=dose_constraint, admin_datetime=admin_datetime)

from glowgreen import cs_restrictions

num_treatments_in_year = 1
df = cs_restrictions(cfit, num_treatments_in_year, admin_datetime)

print(df[["name", "datetime_end"]])
