chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]
chickens2 = [
  { "name": "Margaret", "age": 2, "eggs": 8 },
  { "name": "Hetty", "age": 1, "eggs": 3 },
  { "name": "Henrietta", "age": 3, "eggs": 5 },
  { "name": "Audrey", "age": 2, "eggs": 2 },
  { "name": "Mabel", "age": 5, "eggs": 12 },
]

def egg_count(chickens):
    total_eggs = 0
    for chicken in chickens:
        total_eggs += chicken['eggs']
        chicken['eggs'] = 0
    return total_eggs

eggs_counted = egg_count(chickens)
eggs_counted2 = egg_count(chickens2)

print(f'{eggs_counted} eggs collected')
print(f'{eggs_counted2} eggs collected')