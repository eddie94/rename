import os

global name_list_mp4
global name_list_smi

name_list_mp4=[]
name_list_smi=[]
new_name=[]
cd=str(os.getcwd())
file_name=os.listdir(cd)

#adding mp4 files into list
for filename in file_name:
    ext=os.path.splitext(filename)
    if ext[-1]==".mp4":
        name_list_mp4.append(ext[0])

#adding smi file names
for filename in file_name:
    ext=os.path.splitext(filename)
    if ext[-1]=='.smi':
        name_list_smi.append(filename)

for i in range(len(name_list_mp4)):
    new_name.append(name_list_mp4[i] + '.smi')

for i in range(len(name_list_smi)):
    os.rename(name_list_smi[i],new_name[i])