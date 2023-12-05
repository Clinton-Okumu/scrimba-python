rainy_day = True
cold_day = True
print("Good morning")
if rainy_day:
    print("Bring umbrella and jacket")
elif rainy_day and not(cold_day):
    print("Carry an umbrella and not a jacket")
elif cold_day and not(rainy_day):
    print("Carry a jacket and not an umbrella ")
else:
    print("no need for an umbrella and jacket")