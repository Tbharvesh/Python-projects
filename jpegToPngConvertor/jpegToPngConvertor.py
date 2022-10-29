#Looping through images of one folder,converting to png and saving in another folder 
from PIL import Image 
import os 
import sys
image_folder =input("Enter folder name(adress of image_folder) :")
output_folder =input("Enter output folder name(address of output_folder) :")
d=os.listdir(image_folder)
print(d)
for filename in d:
    img =Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0] 
    print(clean_name) 
    img.save(f'{output_folder}/{clean_name}.png','png') 
