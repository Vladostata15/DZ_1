class Dogs:
    teeths_amount = 42
    tail = 'There is'
    paws_amount = 4

    def __init__ (self, name, age, breed, gender):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender




dog1 = Dogs(name = 'Jack', age = 8, breed = 'German Shepherd', gender = 'Boy')
dog2 = Dogs(name = 'Rex', age = 7, breed = 'Pit bull', gender = 'Boy')
dog3 = Dogs(name = 'Alice', age = 8, breed = 'Akit Nu', gender = 'Girl')


print('Dog 1: ')
print(' ')

print('Name:', dog1.name)
print('Age:', dog1.age)
print('Breed:', dog1.breed)
print('Gender:', dog1.gender)
print('Paws amount:', Dogs.paws_amount)
print('Tail:', Dogs.tail)
print('Teeths amount:', Dogs.teeths_amount)

print(' ')
print(' ')

print('Dog 2: ')
print(' ')

print('Name:', dog2.name)
print('Age:', dog2.age)
print('Breed:', dog2.breed)
print('Gender:', dog2.gender)
print('Paws amount:', Dogs.paws_amount)
print('Tail:', Dogs.tail)
print('Teeths amount:', Dogs.teeths_amount)

print(' ')
print(' ')

print('Dog 3: ')
print(' ')

print('Name:', dog3.name)
print('Age:', dog3.age)
print('Breed:', dog3.breed)
print('Gender:', dog3.gender)
print('Paws amount:', Dogs.paws_amount)
print('Tail:', Dogs.tail)
print('Teeths amount:', Dogs.teeths_amount)