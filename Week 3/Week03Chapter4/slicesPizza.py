pizzas = ['hawaiian','mushroom','cheese','veggie','chicken']

print("The first three items in the list are:")
for pizza in pizzas[0:3]:
    print(pizza.title())

print("The middle three items in the list are:")
for pizza in pizzas[1:4]:
    print(pizza.title())

print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza.title())