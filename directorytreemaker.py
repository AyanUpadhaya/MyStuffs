import os
path=os.getcwd()

#to list root files
list_dir=os.walk(path)

# too see if the root has any files
inner_files=os.listdir(path)

for my_files in inner_files:
    if os.path.isfile(my_files):
        print("File:"+my_files)

#too check if sub directories exists and list them and show them
for root,dirs,files in list_dir:
    for name in dirs:
        print(os.path.join(root,name))
        check_files=os.listdir(os.path.join(root,name))
        if not check_files:
            pass
        else:
            for files in check_files:
                print("-"*len(check_files)+files)

