import os
import time
from PyPDF2 import PdfFileReader

# path = './core_function/images/style_info.txt'
# from PIL import Image
# png = Image.open('images/1.png')
# print (png.size)
pdfimage = PdfFileReader(open('C:/Users/刘志远/Desktop/paper/Transferability in Machine Learning from Phenomena to.pdf', "rb"))
for i in range(pdfimage.getNumPages()):
    page = pdfimage.getPage(i)
    print (page.mediaBox)


# dirss = 'handle_pdf'
# file_path_list = []
# with os.scandir(dirss) as listOfEntries:
#     for entry in listOfEntries:
#         age = time.time() - entry.stat().st_mtime
#         if age < 120:
#             file_path = os.path.join(dirss, entry.name)
#             if os.path.isfile(file_path):
#                 file_path_list.append(file_path)
# print (file_path_list)
