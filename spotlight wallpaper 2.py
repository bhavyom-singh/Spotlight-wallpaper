import os
import shutil
from PIL import Image

##do not alter source
source = "C:/Users/Bhavyom/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"

## temporary destination
os.chdir('C:/Users/Bhavyom/Desktop')
os.mkdir('temp_destination')
temp = "C:/Users/Bhavyom/Desktop/temp_destination/"

## set destination of your choice
destination = "C:/Users/Bhavyom/Desktop/TestPython/"

##empty temp destination
os.chdir(temp)

for each in os.listdir():
    os.remove(each)


##change directory of files to spotlight wallpaper folder
os.chdir(source)

l1 = [file for file in os.listdir()]

##copy file to destination folder
for file in l1:
    shutil.copy2(file,temp)

## change extension to jpg
os.chdir(temp)

jpglist = [allfile for allfile in os.listdir() if len(allfile.split('.'))<2]
for file in jpglist :
    os.rename(file,os.path.splitext(file)[0]+'.jpg') 

for each_file in os.listdir():
    shutil.copy2(each_file,destination)

os.chdir(destination)    
## delete those which are not wallpapers

l2 = [item for item in os.listdir()]
width,height =0,0
for item1 in l2:
    if len(item1.split('.'))<2 or (len(item1.split('.'))>1 and item1.split('.')[1] not in ('jpg','png')):
        l2.remove(item1)
        os.remove(item1)

for item1 in os.listdir():    
        with Image.open(item1) as image:
            width,height = image.size
            image.close()
            if width<500 and height<500:
                l2.remove(item1)
                os.remove(item1)
    
print(os.listdir())
os.chdir(temp)
for each in os.listdir():
    os.remove(each)

os.chdir('..')
os.rmdir(temp)

os.chdir(destination)
print('Total Wallpapers : {}'.format(len(l2)))
