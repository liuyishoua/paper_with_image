import os
from . import my_utils
from . import image2transparent,transparent2pdf
import time
from PyPDF2 import PdfFileWriter, PdfFileReader
# import use the from, or will run bug!!!
# from handle import insert_image2pdf
# root = 'C:/Users/刘志远/Desktop/paper_with_image/core_function'

# provide two methods to handle the file and folder.
# parser = argparse.ArgumentParser()
# parser.add_argument('--style',nargs='+',default=['all'],help='Choose the style for your paper.Including rixi, aoteman, cike, haizei, huyao, shilaimu...')
# parser.add_argument('--folder_name',type = str,default='handle_pdf',help='Choose pdf folder name, default handle_pdf')
# base_info = parser.parse_args()

# make a preprocess.do once and relax all the time.
# deal the paper.
# Two ways: first, do it seperately
# second, do it batch.
def preprocess(image_folder_path,transparent_folder_path,pdf_folder_path,transparent_rate,style_name):
    """this function can be used very rarely.Maybe once for prepare data"""
    # first image to transparent
    image_folder_path = os.path.join(image_folder_path,style_name)
    transparent_folder_path = os.path.join(transparent_folder_path,style_name)
    pdf_folder_path = os.path.join(pdf_folder_path,style_name)
    
    image2transparent.image2transparent(image_folder_path,transparent_folder_path,rate=transparent_rate)
    transparent2pdf.transparent2pdf(transparent_folder_path,pdf_folder_path)

# def return_input_path():
#     pdf_path_list = []
#     first_method = [path for path in os.listdir('.') if os.path.isfile(path)]
#     for path in first_method:
#         # separate by .
#         if os.path.splitext(path)[1] == '.pdf':
#             pdf_path_list.append(path)
#     if input_foldername not in os.listdir('.'):
#         os.makedirs(input_foldername)
    
#     second_method = [os.path.join(input_foldername,path) for path in os.listdir(input_foldername) if os.path.isfile(os.path.join(input_foldername,path))]
#     for path in second_method:
#         if os.path.splitext(path)[1] == '.pdf':
#             pdf_path_list.append(path)
#     return pdf_path_list

# input: files and style_list
# style_root like this 'images/pdf'
def handle_file(input_file,style_list,style_root):
    output_file = PdfFileWriter()
    page_count = input_file.getNumPages()

    style_path_list = my_utils.get_style_list_path(style_list,style_root)
    style_pdf_path = my_utils.get_style_pdf_path(style_path_list)

    final_pdf_path = my_utils.get_random_list(style_pdf_path,page_count)
    for i in range(page_count):
            pdfimage = PdfFileReader(open(final_pdf_path[i], "rb"))
            output_file.addPage(input_file.getPage(i))
            output_page = output_file.getPage(output_file.getNumPages()-1)    
            output_page.mergePage(pdfimage.getPage(0))
            if i == page_count-1:
                    print (f'All page is {page_count} page, have already load successfully')
    return output_file

# input_paths = return_input_path()
# output_root = 'results'
# for input_path in input_paths:
#     start = time.time()
#     output_name = utils.get_file_name(input_path)
#     insert_image2pdf(input_path,output_path=os.path.join(output_root,output_name+'.pdf'),style_path_list=style_list_path)
#     end = time.time()
#     print (f'complete the {output_name}.pdf using {end - start} s')

# print ('shu shu a yi chu guo le !!!')



