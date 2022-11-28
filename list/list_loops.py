guests=['akmal','said','lenur']
print(guests[0],'I am inviting you to the party')
print(f'Hello {guests[0].title()}, I am inviting you to the party.')
print(f'Hello {guests[1].title()}, I am inviting you to the party.')
print(f'Hello {guests[2].title()}, I am inviting you to the party.')
print('Hello '+ guests[0].title()+', I am inv')

# a = 'said'
removed_guest= guests.pop(1)
print(f'{removed_guest},cant make it to the party')
print (guests)
guests.append('max')
print(guests)
print(f'Hello {guests[0].title()}, Welcome to the party')
print(f'Hello {guests[1].title()}, Welcome to the party')
print(f'Hello {guests[2].title()}, Welcome to the party')
guests.insert(0,'marina')
guests.insert(2,'kalina')
guests.insert(5,'darina')
print(guests)
print(f'Hello {guests[0].title()}, I am inviting you to the party')

removed_guest=guests.pop(5)
print(removed_guest)
print(f'Dear, {removed_guest.title()}, sorry we removed you from list')


#3-8
towns=('tokio', 'paris','a_tashkent','san-francisco')
print(towns)

print(sorted(towns))

print(towns)

print(sorted(towns,reverse=True))
print(towns)


print(towns.__reversed__())



