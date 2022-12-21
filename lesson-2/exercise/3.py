import os
import sys
import shutil
if len(sys.argv)==3: 
    base_dir = sys.argv[1]
    file_extension = sys.argv[2]#decide extension fo file to copy

    backup_dir = r"C:\Users\Tia"
    dimension = 0
    
    for dirpath, dirs, files in os.walk(base_dir):
        """for dir in dirs:
            print(dirpath, dir)"""
        for file in files:
            current_file = os.path.join(dirpath, file)
            if current_file.endswith(file_extension):
                dimension += os.path.getsize(current_file)
                relative_current_path = os.path.relpath(current_file, base_dir )
                backup_current_path_file = os.path.join(backup_dir,relative_current_path)
                backup_current_path = os.path.join(backup_current_path)
                if not os.path.isdir(backup_current_path):
                    os.makedirs(backup_current_path)
                shutil.copyfile(current_file,backup_current_path_file)
    
    print(f"dimension of {base_dir} = {round(dimension/1024,2)} Mb")
else:
    sys.stdout.write("Directory param missing")
