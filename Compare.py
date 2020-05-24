# Comparetor Program
import os

Name = input('User Name: ')

#Pass = input('Password :')

Directory_Name = Name

parent_dir = 'D:\Storage'

path = os.path.join(parent_dir, Directory_Name)

os.mkdir(path)  

print("Directory_Name '% s' created" % Directory_Name)