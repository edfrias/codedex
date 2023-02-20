credits = int(input('Enter you total credits '))
height = int(input('Enter your current height '))
with_taller_person = False

# Not working properly :(


def has_adult():
    global with_taller_person
    adult = bool(input('Are you with a taller person? y/n '))
    if adult == 'y':
        print('you are with a taller person')
        with_taller_person = True
    elif adult == 'n':
        print('you are alone')
        with_taller_person = False
    return with_taller_person


if credits < 10:
    print("You don't have enough credits to ride")

if height >= 137 and credits >= 10:
    print('Ejoy your ride!')

if height < 137:
    has_adult()
    if height < 100 and not with_taller_person:
        print("You're not tall enough for this ride yet.")
    elif height >= 100 and with_taller_person:
        print("Enjoy the ride!")
