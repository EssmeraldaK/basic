pizzas=['piz1','piz2','piz3','piz4','piz5']
print(pizzas[0:3])
print('***********')
print(pizzas[1:-1])
for pizza in pizzas[0:]:
 print(f'we have {pizza} pizza today')

new_pizzas = pizzas
copy_pizzas = pizzas[:]
print(f'list before updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}')
pizzas.append('cruasan')
new_pizzas.append('carrot')
copy_pizzas.append('mazarella')
copy_pizzas.append('pumpkin')
print(f'list after updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}')

print('Tuples')
animals = ('dog','cat','horse')
dog_index = animals.index('dog')
print((f'index of dog element in the tuple:{dog_index}'))
sorted_animals=sorted(animals)
print(f'sorted animals: {sorted_animals}')
for animal in sorted_animals[0:2]:
 print(f'each animal:{animal}')






