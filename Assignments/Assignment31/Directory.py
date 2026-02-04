import os
import shutil

###########################################################################
# Function name: FileSearch
# Parameters: DirName = Path to the existing directory
#             ExtName = File extension to search for (e.g., '.txt') 
# Output: A file named Result.log in the script's directory.
#
# Description: Scans the target directory and its subdirectories for files 
# with a specific extension. It generates a comprehensive list of matches 
# and records them in Result.log.
#
# Author: Prasad Sampat Sarwar
# Date: 4 Feb 2026
###########################################################################

def FileSearch(DirName, ExtName):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if(ExtName[0] != "."):
        print("Invalid Extension!!")
        return

    fobj = open("Result.log","w")

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for Fname in FileName:
            _, Ext = os.path.splitext(Fname)
            
            if(Ext == ExtName):
                fobj.write(Fname+"\n")

    fobj.close()

###########################################################################
###########################################################################
# Function name: RenameFiles
# Parameters:    DirName = Path to the target directory (string)
#                Ext1    = Current file extension to search for (e.g., '.txt')
#                Ext2    = New file extension to apply (e.g., '.doc')
#
# Return:        None (Generates 'Result.log' in the current directory)
#
# Description:   Recursively traverses the specified directory to find files 
#                with Ext1 and renames them to Ext2. All renaming actions 
#                are logged to 'Result.log' with original and new paths.
#
# Author:        Prasad Sampat Sarwar
# Date:          4 Feb 2026
###########################################################################

def RenameFiles(DirName,Ext1,Ext2):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if((Ext1[0] != ".") or (Ext2[0] != ".")):
        print("Invalid Extension!!")
        return
    
    fobj = open("Result.log","w")
    
    for Folder, SubFolder, File in os.walk(DirName):
        for Fname in File:
            Name , Extionsion = os.path.splitext(Fname)
            
            if(Extionsion == Ext1):
                OldPath = os.path.join(Folder,Fname)

                NewName =  Name + Ext2
                NewPath = os.path.join(Folder,NewName)

                fobj.write("Renamed: "+OldPath+" to "+NewPath+"\n")

                os.rename(OldPath,NewPath)
    fobj.close()

###########################################################################
###########################################################################
# Function name: CopyFiles
# Parameters:    DirName    = Name of the existing source directory
#                NewDirName = Name of the destination directory
#
# Return:        None (Copies files and subdirectories to the new location)
#
# Description:   Recursively traverses the source directory and replicates its 
#                entire internal structure within the destination directory. 
#                It ensures all subfolders are created and files are copied 
#                with their original metadata preserved.
#
# Author:        Prasad Sampat Sarwar
# Date:          4 Feb 2026
###########################################################################

def CopyFiles(DirName,NewDirName):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for Folder, SubFolder, File in os.walk(DirName):
        for Fname in File:

            OldPath = os.path.join(Folder,Fname)
            rel_path = os.path.relpath(Folder,DirName)
            NewPath = os.path.join(NewDirName,rel_path)

            os.makedirs(NewPath,exist_ok=True)
            shutil.copy2(OldPath, NewPath)

###########################################################################
###########################################################################
# Function name: CopyFilesExt
# Parameters:    DirName    = Path to the existing source directory
#                NewDirName = Path to the destination directory
#                Ext        = Specific file extension to filter (e.g., '.py')
#
# Return:        None (Copies filtered files to the destination)
#
# Description:   Selectively clones files from a source to a destination 
#                based on a file extension. It maintains the original 
#                directory hierarchy by recreating subfolders within the 
#                target directory for every matching file found.
#
# Author:        Prasad Sampat Sarwar
# Date:          4 Feb 2026
###########################################################################

def CopyFilesExt(DirName,NewDirName,Ext):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if(Ext[0] != "."):
        print("Invalid Extension!!")
        return

    
    for Folder, SubFolder, File in os.walk(DirName):
        for Fname in File:
            _, extn = os.path.splitext(Fname)
            
            if(extn == Ext):
                OldPath = os.path.join(Folder,Fname)
                rel_path = os.path.relpath(Folder,DirName)
                NewPath = os.path.join(NewDirName,rel_path)

                os.makedirs(NewPath,exist_ok=True)
                shutil.copy2(OldPath, NewPath)

###########################################################################
