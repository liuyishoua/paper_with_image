# hahhaha,ceshi1
import os
import time

path = './core_function/images/style_info.txt'

with open(path,'a') as file:
    file.write('\n'+'haha'+' '+'哈哈')
    # for i in range(2):
    #     file.write('我 是\n')
    # print (lines)

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
