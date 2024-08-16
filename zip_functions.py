import zipfile
import types
import os


# https://stackabuse.com/creating-a-zip-archive-of-a-directory-in-python/
def ZipDirectory(directory_paths, zip_path):
    # Convert str to list
    if isinstance(directory_paths, str):
        directory_paths = [directory_paths]
        
    if isinstance(directory_paths, list):   
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for directory_path in directory_paths:
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        print( os.path.join(root, file) )
                        zipf.write(
                            os.path.join(root, file), 
                            os.path.relpath(
                                os.path.join(root, file), 
                                os.path.join(directory_path, '..')
                            )
                        )

# All 3 options below works
# directory_paths, can be ether a str "" or a list of strings []
ZipDirectory( ["/home/user/folder1", "/home/user/folder2"], "/home/user/backup.zip")
ZipDirectory( ["/home/user/folder2"], "/home/user/backup.zip")
ZipDirectory( "/home/user/folder2", "/home/user/backup.zip")



# Restore backup
# Loading the backup.zip and creating a zip object 
# https://www.geeksforgeeks.org/unzipping-files-in-python/
with zipfile.ZipFile( "/home/user/backup.zip", 'r') as zObject:
    # Extracting all the members of the zip into a specific location. 
    zObject.extractall( path="/home/user" )  
zObject.close()
