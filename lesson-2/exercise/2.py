import sys
import os
#file py1
print("=> ", sys.argv)
if( len(sys.argv)>2):
    sys.stdout.write("TEST OUT")
    print(sys.argv[1])
else:
    print('Format error')

#file py2
inflow = sys.stdin.read(1) #read only 1 char from 
print("IN => ",inflow)

#file py3
sys.stderr.write("ERROR XXX")
#os.system("start win.ini")
#os.makedirs(r"c:\export\test\christian")
os.system(r"start win.ini")#raw command
dirs = os.listdir(r"C:\Users\Tia")
print(dirs)#list of all files contained into this directory

#file py4
dimension = 0
base_path = r"C:\Users\Tia"
all_files_in_base_path = os.listdir(base_path)
for file in all_files_in_base_path:
    file_full_path = os.path.join(base_path, file)
    if os.path.isfile(file_full_path):
        dimension += os.path.getsize(file_full_path)
        print(file_full_path)

print(f'dimension of {base_path} = {dimension/1024}MB')

#file py5
#if len(sys.argv)==3: 
    #base_dir = sys.argv[1]
base_dir = r"C:\Users\Tia"
for dir_path, dir_names, files in os.walk(base_dir):
    #for dir in dir_names:
        #print(os.path.join(dir_path,dir)) ##all directory 
    for file in files:
        #print(os.path.join(dir_path,file)) ##all file 
        current_file = os.path.join(dir_path,file)
        dimension += os.path.getsize(current_file)
        print(f'{current_file} has this dimension {round(dimension/1024,2)} MB')

print(f"dimension of {base_dir} = {round(dimension/1024,2)} Mb")
    
#file 6py
