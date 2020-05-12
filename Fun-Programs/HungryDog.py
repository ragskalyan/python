# Hungry Pets Program
''' There is a Boss, Dog named as Julie & Cat named as Chowzi. The Boss task is feeding food to his pets'''
# Variables Declaration
''' Declared as respective values for each one of them'''
Dog_Name, Cat_Name, Boss_Name = 'Julie','ChowZi','Sam'
''' Variables declared separately'''
#Dog_Name = 'Julie'
#Cat_Name = 'ChowZi'
#Boss_Name = 'Sam'
'''Here, I have used String,lists, tuples & dictionary data types & len function and also three types of print with f-string method & concordinates'''
print (f"{Dog_Name}: Hello Boss, I am feeling hungry....Wakeup")
print (f"{Boss_Name}: Hello {Dog_Name} & {Cat_Name}, Good Morning")
print (f'''{Boss_Name}: Lemme See, {Dog_Name}''')
print (f'{Dog_Name}: Fast fast....\n\tI have eat something now...\n{Boss_Name}: Wait dear {Dog_Name} let me check\n{Cat_Name}: Meow....\n{Boss_Name}: Okay...{Cat_Name} you also wakeup now')

# List & Ditionary
foodlist = ['Bone', 'Bread', 'Egg', 'Juice', '{"Fruits": ["Oragne", "Apple", "Grapes", "Kiwi"]}', 'Chicken', 'Milk']
Nooffood = len(foodlist)

print (f'{Boss_Name}: Hey {Dog_Name}, There are total {Nooffood} food items we have \n{Dog_Name}: What we have? \n{Boss_Name}: We have ' + str(foodlist[0:3]) + ' and ' + str(foodlist[-2:-1]) + f'and for our {Cat_Name} we have ' + str(foodlist[-1]) +f'\n{Dog_Name}: Wow.... I need my fav '+ str(foodlist[0]))
print (f'{Boss_Name}: Okay {Dog_Name} ' + '\n\tTake this ' + str(foodlist[0])+f'\n\tHey {Cat_Name}, Come and have ' + str(foodlist[-1]) + f'\n{Cat_Name}: Meow....')
