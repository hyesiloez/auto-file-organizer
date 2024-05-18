import os
import shutil

def createFolder(fpath,subfolder_name):
    os.makedirs(os.path.join(fpath,subfolder_name))
    return os.path.join(fpath,subfolder_name)

def clean(fpath):
    for filename in os.listdir(fpath):
        if os.path.isfile(os.path.join(fpath,filename)):
            ending = filename.split(".")[-1]
            subfolder_name = f"{ending.upper()} Files"
            if not os.path.exists(os.path.join(fpath,subfolder_name)):
                subfolder_name = f"{ending.upper()} Files"
                subfolder = createFolder(fpath, subfolder_name)
            else :
                subfolder = os.path.join(fpath,subfolder_name)
            pathOfFile = os.path.join(fpath,filename)
            shutil.move(pathOfFile, subfolder)
            print(f"Moved {filename} to {subfolder_name}")


        else:
            continue






if __name__ == "__main__":
    print("Cleaning: ")
    fpath = "/Users/halil/OneDrive/Dokumente/Personal"
    if os.path.exists(fpath):
        clean(fpath)
        print("Cleaning Done")
    else:
        print("Path does not exist")