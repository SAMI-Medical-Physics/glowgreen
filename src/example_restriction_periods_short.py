from glowgreen import cs_restrictions, Clearance_1m
from datetime import datetime

num_treatments_in_year = 1

dose_rate_init_xm = 5.7  # uSv/h
effective_half_life = 60  # h
distance = 1  # m

# admin at noon
admin_datetime = datetime(day=25, month=12, year=2021, hour=12, minute=0)

# cfit = Clearance_1m('biexponential', [dose_rate_init_xm, fraction1, half_life1, half_life2],
#    distance)

cfit = Clearance_1m("exponential", [dose_rate_init_xm, effective_half_life], distance)

df = cs_restrictions(cfit, num_treatments_in_year, admin_datetime)

print(df[["name", "restriction_period", "dose"]])
# print(df.columns)
