planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet_to_initial = {planet: planet[0] for planet in planets}

# print(planet_to_initial)

for p in planet_to_initial:
    pass
    #print(p, planet_to_initial[p])

print(dict.keys(planet_to_initial))
print(sorted(dict.values(planet_to_initial)))
