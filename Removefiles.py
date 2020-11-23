import os
import shutil
import time

days=30
path="c-99/FolderC/S.txt"
seconds=time.time()-(days*24*60*60)
if os.path.exists(path):
    shutil.rmtree() 
    for files in os.walk(path):
        info=os.listOfFiles
        print(info)