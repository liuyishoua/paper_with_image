import os
from . import my_utils
import img2pdf

def transparent2pdf(image_folderpath,output_folderpath):
    # if the corresponding pdf has files, delete it or we will meet the trouble
    # my_utils.del_folder_files(output_folderpath)

    if not os.path.exists(output_folderpath):
        os.makedirs(output_folderpath)
    # if transparent age is below 2 minites, we can get the transparent to pdf
    files_path = my_utils.get_2minite_folder_filepath(image_folderpath)
    for path in files_path:
        file_name = my_utils.get_file_name(path)
        output_path = os.path.join(output_folderpath,file_name+'.pdf')
        if os.path.exists(output_path):
            os.remove(output_path)
        with open(output_path,'wb') as file:
            file.write(img2pdf.convert(path))


if __name__ == '__main__':
    transparent2pdf('./images/transparent/rixi','./images/pdf/rixi')