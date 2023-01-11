gryffindor = ravenclaw = hufflepuff = slytherin = 0

q1 = int(input('Do you like Dawn or Dusk? \n1) Dawn  \n2) Dusk \n'))

if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input')

q2 = int(input('When I\'m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \n'))

if q2 == 1:
    hufflepuff += 1
elif q2 == 2:
    slytherin += 1
elif q2 == 3:
    ravenclaw += 1
elif q2 == 4:
    gryffindor += 1
else:
    print('Wrong input')

q3 = int(input('Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n'))

if q3 == 1:
    slytherin += 1
elif q3 == 2:
    hufflepuff += 1
elif q3 == 3:
    ravenclaw += 1
elif q3 == 4:
    gryffindor += 1
else:
    print('Wrong input')


print('Gryffindor: ', gryffindor)
print('Ravenclaw: ', ravenclaw)
print('Hufflepuff: ', hufflepuff)
print('Slytherin: ', slytherin)


if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print('\nGryffindor must be')
elif ravenclaw > hufflepuff and ravenclaw > slytherin:
    print('\nRavenclaw must be')
elif hufflepuff > slytherin:
    print('\nHufflepuff must be')
else:
    print('\nSlytherin must be')
