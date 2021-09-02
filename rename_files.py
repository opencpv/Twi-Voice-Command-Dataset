import numpy as np
import pandas as pd
import shutil
import os

data_dir = './all_data/'
new_data_dir = './all_data_common_names/'
counter = 1
# Get list of files in original directory
files = os.listdir(data_dir)
total_file_num = len(files)
progress = 0

def PrintProgress(current,total):
    percentage = round((current/total)*100,2)
    print(percentage)

for file in files:
    file_directory = data_dir+file
    file_name = file.split('_')[0].lower()
    if file_name=='yes':
        new_name = "yes_"+str(counter)+'.ogg'
        new_dir = new_data_dir+new_name
        shutil.copy(file_directory,new_data_dir)
        os.rename(new_data_dir+file,new_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    elif file_name=='no':
        new_name = "no_"+str(counter)+'.ogg'
        new_dir = new_data_dir+new_name
        shutil.copy(file_directory,new_data_dir)
        os.rename(new_data_dir+file,new_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    elif file_name=='on':
        new_name = "on_"+str(counter)+'.ogg'
        new_dir = new_data_dir+new_name
        shutil.copy(file_directory,new_data_dir)
        os.rename(new_data_dir+file,new_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    else:
        new_name = "off_"+str(counter)+'.ogg'
        new_dir = new_data_dir+new_name
        shutil.copy(file_directory,new_data_dir)
        os.rename(new_data_dir+file,new_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    counter +=1

print('File copy complete')

