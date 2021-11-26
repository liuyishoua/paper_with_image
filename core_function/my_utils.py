import os
import glob
import time
import random

def get_style_pdf_path(style_list_path):
    style_pdf_path = []
    for paths in style_list_path:
        style_pdf_path = style_pdf_path + [os.path.join(paths,path) for path in os.listdir(paths)]
    return style_pdf_path

def get_style_list_path(style_list,root):
    style_list_path = []
    for style in style_list:
        style_list_path.append(os.path.join(root,style))
    return style_list_path

def get_random_list(list,numbers):
    # can be sampled duplicates
    return random.choices(list,k=numbers)

def get_folder_number(path):
    # path = './images/pdf'
    number = len([name for name in os.listdir(path) if os.path.isfile(path+os.sep+name)])
    print (f'{path} have {number} files')
    return number

def get_folder_filepath(path):
    """return files list path"""
    # path = './images/pdf'
    file_path_list = [path+os.sep+name for name in os.listdir(path) if os.path.isfile(path+os.sep+name)]
    return file_path_list

def get_2minite_folder_filepath(path):
    """return the before 2 minites files not including folder"""
    dirss = path
    file_path_list = []
    with os.scandir(dirss) as listOfEntries:
        for entry in listOfEntries:
            age = time.time() - entry.stat().st_mtime
            if age < 120:
                file_path = os.path.join(dirss, entry.name)
                if os.path.isfile(file_path):
                    file_path_list.append(file_path)
    return file_path_list

def get_folder_filename(path):
    """return all file names"""
    # path = './images/pdf'
    file_name = [name for name in os.listdir(path) if os.path.isfile(path+os.sep+name)]
    return file_name

def get_file_name(path):
    """return if C:\\Users\\刘志远\\Desktop\\paper_with_image.pdf, get the paper_with_image as return"""
    no_suffix = os.path.splitext(path)[0]
    name = os.path.basename(no_suffix)
    return name

def del_folder_files(path):
    # path = './images/pdf'
    path = path +'/*'
    # is similar as os.listdir
    files = glob.glob(path)
    for f in files:
        if os.path.isfile(f):
            os.remove(f)
    print (f'delete {path} files successfully')

# del_folder_files('./images/pdf')