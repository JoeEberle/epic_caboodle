class file_mamager(object):
    import os
    import glob
    from shutil import copyfile, copytree


def create_directory(directory_path):
    ''' the create_directory function will create a driectory if it doesnt already exist ''' 
    import os  
    try:
        os_stat = os.mkdir(directory_path)
    except:
        status = "Error attempting to create directory:{}".format(directory_path)
    else:
        status = "Directory:{} created".format(directory_path)
    return(status) 

def copy_all_files(path, extension, target_dir):
    ''' the copy_all_files function will copy all the files of a specific type (extension) to a target directory ''' 
    import os, glob
    from shutil import copyfile, copytree    
    status = '\nDisovering files of extension:{} in directory:{} to move to directory{} '.format(extension, path, target_dir) 
    os.chdir(path)
    file_count = 0
    for file in glob.glob('*.{}'.format(extension)):
        file_count += 1
        target_file = target_dir + file
        copyfile(file, target_file)
        status =  status  + '\nFile #{} copying file {} to {} '.format(file_count, file, target_file)
    return(status) 

def list_all_files(path, extension):
    ''' the list_all_files function will discover and return a list of files of a specific file type in a string'''
    import os, glob 
    os.chdir(path)
    file_count = 0
    for file in glob.glob('*.{}'.format(extension)):
        file_count += 1 
        status =  status + '\nFound File:#{} Filename:{} '.format(file_count, file)
    return(status)

def copy_and_rename_all_files(path, old_ext, new_ext):
    ''' the copy_and_rename_all_files function will copy and rename the extension of files of a specific type'''   
    import os, glob 
    from shutil import copyfile, copytree
    status = '\nDiscovering files of extension: {} in directory: {} '.format(old_ext, path) 
    os.chdir(path)
    file_count = 0
    for file in glob.glob('*.{}'.format(old_ext)):
        file_count += 1 
        copyfile(file, file.replace('py','jaepy'))
        status =  status + '\nFile #{} copy-rename:{} to:{}'.format(file_count, file,file.replace(old_ext,new_ext)) 
    return(status) 