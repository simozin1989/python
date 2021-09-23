import os
import shutil


dir_path = os.path.dirname(os.path.realpath(__file__))


       

for fileName in os.listdir(dir_path): 
     if fileName.endswith(("pdf")):
         if not os.path.exists("pdf"):
             os.makedirs("pdf")
             shutil.copy2(fileName,"pdf")
             os.remove(fileName)
            
     if fileName.endswith((".png", ".jpg")):
        if not os.path.exists("Images"):
             os.makedirs("Images")
             shutil.copy2(fileName,"Images")
             os.remove(fileName)
             print('hhhhhhhhhhhhhhhhhhhhhhhh')
   