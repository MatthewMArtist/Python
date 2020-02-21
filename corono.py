starting_numbers = 10


infected = starting_numbers + spread_per_day
dead = infected / 50


time_days = 6


spread_per_day = infected * transmission_rate * time_days/12
transmission_rate = 2.2


print("{} infected people".format(infected))
print("{} people dead"(dead))






