
sugar = 12
print(f"INITIAL SUGAR VALUE:{sugar}")
print(f"ID SUGAR VALUE:{id(sugar)}")
sugar = 22
print(f"SECONDARY SUGAR VALUE:{sugar}")
print(f"ID OF  SUGAR VALUE:{id(sugar)}")
spice_mix = set()
print(f"The value of spice is:{id(spice_mix)}")
spice_mix.add("ginger")
spice_mix.add("garlic")
spice_mix.add("pepper")
print(f"The value of spice is:{id(spice_mix)}")
print(f"The holding of spice is:{spice_mix}")