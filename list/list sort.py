
cars = ['tesla','bmw','moskvich','lexus']
print('Permanent sorting - sort().')
print('List before sorting:',cars)
cars.sort()
print("list after sorting: ",cars)

names = ['john','jane', 'mark']
print ('List before sorting: ',names)
names.sort(reverse=True)
print('List after sorting: ',names)

print('sorting temporarily-sorted() ')
car_models=( 'kia','toyota','audi','subaru')
print('car models before sorting:', car_models)
sorted_car_models_asc= sorted(car_models)
sorted_car_models_dsc= sorted(car_models, reverse=True)

print('sorted car models after sorting in ascending order: ',sorted_car_models_asc)
print('sorted car models after sorting in descending order: ',sorted_car_models_dsc)