name = input ('What is your first name?')
distance_in_km = input ('Distance you have covered in km ?')
distance_in_miles = float(distance_in_km) / 1.609
print(f'Hi {name.title()}! {distance_in_km} km is equivalent to {round(distance_in_miles, 1)} miles.')