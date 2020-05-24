# Control Flow Program
# For Loop

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print (num)

for num in mylist:
    # Check Even & Odd numbers in my list
    if num %2 == 0:
        print ('Even Number '+str(num))
    else:
        print (f'Odd Number '+str(num))

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    print (list_sum)

# Benifits of tuples in For loops

tpl = (1,2,3)

for num in tpl:
    print(num)

# tuples in list & unpacking tuples using for loops

tlist = [(1,2),(3,4),(5,6),(7,8)]

for x in tlist:
    print(x)

for (x,y) in tlist:
    print (x)
    print (y)

tlist2 = [(1,2,'a'),(3,4,'b'),(5,6,'c'),(7,8,'d')]

for (x,y,z) in tlist2:
    print (x)
    print (y)
    print (z)

# dictionary

d = {'k1':1,'k2':2,'k3':3}

for x in d:
    print(x)

# Tuples Unpacking

for key,value in d.items():
    print (value)