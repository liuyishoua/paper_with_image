import os
import utils
from PyPDF2 import PdfFileWriter, PdfFileReader
from utils import get_random_list, get_style_pdf_path
# this py file work has transfer to the main.py

def insert_image2pdf(input_path,output_path,style_path_list):
        # input_path = '1.pdf'
        # output_path = '1_handle.pdf'
        # pdfimage_path = 'images/pdf'
        input_file = PdfFileReader(open(input_path, "rb"))
        output_file = PdfFileWriter()
        page_count = input_file.getNumPages()
        
        style_pdf_path = get_style_pdf_path(style_path_list)
        final_pdf_path = get_random_list(style_pdf_path,page_count)
        for i in range(page_count):
                pdfimage = PdfFileReader(open(final_pdf_path[i], "rb"))
                output_file.addPage(input_file.getPage(i))
                output_page = output_file.getPage(output_file.getNumPages()-1)    
                output_page.mergePage(pdfimage.getPage(0))
                if i == page_count-1:
                        print (f'All page is {page_count} page, have already load successfully')

        with open(output_path, "wb") as outputStream:
                output_file.write(outputStream)

# def insert_image2pdf(input_path,output_path,style_path_list):
#         # input_path = '1.pdf'
#         # output_path = '1_handle.pdf'
#         # pdfimage_path = 'images/pdf'
#         input_file = PdfFileReader(open(input_path, "rb"))
#         output_file = PdfFileWriter()
#         page_count = input_file.getNumPages()
        
#         style_pdf_path = get_style_pdf_path(style_path_list)
#         final_pdf_path = get_random_list(style_pdf_path,page_count)
#         for i in range(page_count):
#                 pdfimage = PdfFileReader(open(final_pdf_path[i], "rb"))
#                 output_file.addPage(input_file.getPage(i))
#                 output_page = output_file.getPage(output_file.getNumPages()-1)    
#                 output_page.mergePage(pdfimage.getPage(0))
#                 if i == page_count-1:
#                         print (f'All page is {page_count} page, have already load successfully')

#         with open(output_path, "wb") as outputStream:
#                 output_file.write(outputStream)

# if __name__ == '__main__':
#         insert_image2pdf('./1.pdf','./results/1.pdf',style_path_list=utils.get_style_list_path(['cike','haizei','huyao'],'./images/pdf'))
