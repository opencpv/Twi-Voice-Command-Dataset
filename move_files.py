import numpy as np
import pandas as pd
import shutil
import os

data_dir = './data/'
on_folder_dir = './twi_command_dataset/on'
off_folder_dir = './twi_command_dataset/off'
yes_folder_dir = './twi_command_dataset/yes'
no_folder_dir = './twi_command_dataset/no'

# Get list of files in original directory
files = os.listdir(data_dir)
total_file_num = len(files)
progress = 0

def PrintProgress(current,total):
    percentage = round((current/total)*100,2)
    print(percentage)

for file in files:
    file_directory = data_dir+file
    file_name = file.split('_')[0]
    if file_name=='yes':
        shutil.copy(file_directory,yes_folder_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    elif file_name=='no':
        shutil.copy(file_directory,no_folder_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    elif file_name=='on':
        shutil.copy(file_directory,on_folder_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1
    else:
        shutil.copy(file_directory,off_folder_dir)
        PrintProgress(progress,total_file_num)
        progress=progress+1

print('File copy complete')

