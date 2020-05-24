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
print ("{}: Hello Boss, I am feeling hungry....Wakeup".format(Dog_Name))
print ("{0}: Hello {1} & {2}, Good Morning".format(Boss_Name,Dog_Name,Cat_Name))
print ('''{0}: Lemme See, {1}'''.format(Boss_Name,Dog_Name))
print ('{0}: Fast fast....\n\tI have eat something now...\n{1}: Wait dear {2} let me check\n{3}: Meow....\n{4}: Okay...{5} you also wakeup now'.format(Dog_Name,Boss_Name,Dog_Name,Cat_Name,Boss_Name,Cat_Name))

# List & Ditionary
foodlist = ['Bone', 'Bread', 'Egg', 'Juice', '{"Fruits": ["Oragne", "Apple", "Grapes", "Kiwi"]}', 'Chicken', 'Milk']
Nooffood = len(foodlist)

print (('{0}: Hey {1}, There are total {2} food items we have \n{3}: What we have? \n{4}: We have '.format(Boss_Name,Dog_Name,Nooffood,Dog_Name,Boss_Name)) + str(foodlist[0:3]) + ' and ' + str(foodlist[-2:-1]) + ('and for our {} we have '.format(Cat_Name)) + str(foodlist[-1]) +('\n{}: Wow.... I need my fav '.format(Dog_Name))+ str(foodlist[0]))
print (('{0}: Okay {1} '.format(Boss_Name,Dog_Name)) + '\n\tTake this ' + str(foodlist[0])+('\n\tHey {}, Come and have '.format(Cat_Name)) + str(foodlist[-1]) + ('\n{}: Meow....'.format(Cat_Name)))