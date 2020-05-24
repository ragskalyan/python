import os

Directory_Name = "Kalyan"

parent_dir = 'D:\Storage'

path = os.path.join(parent_dir, Directory_Name)

os.mkdir(path)  

print("Directory_Name '% s' created" % Directory_Name)