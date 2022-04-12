from glowgreen import cs_patterns, ContactPatternRepeating, ContactPatternOnceoff, Clearance_1m
from datetime import datetime

num_treatments_in_year = 1

dose_rate_init_xm = 5.7  # uSv/h
effective_half_life = 60  # h
distance = 1  # m

# admin at noon
admin_datetime = datetime(day=25, month=12, year=2021, hour=12, minute=0)

# go
#cfit = Clearance_1m('biexponential', [dose_rate_init_xm, fraction1, half_life1, half_life2], 
#    distance)

cfit = Clearance_1m('exponential', [dose_rate_init_xm, effective_half_life], 
    distance)

df = cs_patterns()

df['dose_constraint_corrected'] = df['dose_constraint'] / num_treatments_in_year
df.loc[df['per_episode']==1, ['dose_constraint_corrected']] = df['dose_constraint']

tau_column = []
dose_column = []
datetime_end_column = []
for _, row in df.iterrows():
    if row['pattern_type'] == 'repeating':
        cpat = ContactPatternRepeating(row['theta'], row['c'], row['d'])
        tau, dose, datetime_end = cpat.get_restriction(cfit, row['dose_constraint_corrected'], admin_datetime, next_element=True)
    elif row['pattern_type'] == 'onceoff':
        cpat = ContactPatternOnceoff(row['theta'], row['c'], row['d'])
        tau, dose, datetime_end = cpat.get_restriction(cfit, row['dose_constraint_corrected'], admin_datetime)

    #tau_column.append(tau / 24.)  # h -> d
    tau_column.append(tau)
    dose_column.append(dose)
    datetime_end_column.append(datetime_end)

df['restriction period (h)'] = tau_column
df['dose (mSv)'] = dose_column
df['datetime_end'] = datetime_end_column

df[['name', 'restriction period (h)', 'dose (mSv)']].to_csv('restrictions_2nd_Zr_mAb.csv', index=False)