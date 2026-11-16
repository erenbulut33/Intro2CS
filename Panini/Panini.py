mine = {"Pierogi", "Sarma", "Borscht", "Dolma", "Zapiekanka"}
friend = {"Sushi", "Tacos", "Borscht", "Dolma", "Pizza"}

print("Our favorite foods are:")
print(mine.union(friend))

print("Our common favorite foods are:")
print(mine.intersection(friend))

print("Foods I like but my friend doesn't:")
print(mine.difference(friend))

print("Foods only one of us likes:")
print(mine.symmetric_difference(friend))