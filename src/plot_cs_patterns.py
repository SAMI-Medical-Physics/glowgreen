from glowgreen import cs_patterns, ContactPatternRepeating, ContactPatternOnceoff

df = cs_patterns()

for _, row in df.iterrows():
    if row['pattern_type'] == 'repeating':
        cpat = ContactPatternRepeating(row['theta'], row['c'], row['d'])
    elif row['pattern_type'] == 'onceoff':
        cpat = ContactPatternOnceoff(row['theta'], row['c'], row['d'])

    cpat.plot(name=row['name'])