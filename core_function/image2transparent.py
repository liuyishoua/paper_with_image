import os
from . import my_utils
from PIL import Image

def image2transparent(image_folder_path,output_folder_path,rate = 0.5):
    # record the info of rate in output folder
    # with open(os.path.join(output_folder_path,'log.txt'),'w') as file:
    #     file.write(f'the transparent of image is {rate}\n')
    # accroding the size of image, to design a adptative method
    w ,h= 1800,1200
    w1,h1 = 800,1200
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)
    # if image age is below 2 minites, we can get the image to transparent
    folder_filespath = my_utils.get_2minite_folder_filepath(image_folder_path)
    for iter,file_path in enumerate(folder_filespath):
        img = Image.open(file_path)
        x_s, y_s = img.size
        if x_s > y_s:
            img = img.resize((w,h))
        else:
            img = img.resize((w1,h1))
        img = img.convert("RGBA")
        x, y = img.size # 获得长和宽
        transparent = int(256*rate)
        # 设置每个像素点颜色的透明度
        for i in range(x):
            for k in range(y):
                color = img.getpixel((i, k))
                color = color[:-1] + (transparent, )
                img.putpixel((i, k), color)
        save_path = os.path.join(output_folder_path,my_utils.get_file_name(file_path)+'.png')
        if os.path.exists(save_path):
            os.remove(save_path)
        img.save(save_path,'png')
        print(f"the {iter+1}th image to transparent Successful,rate is {rate}")

# 设置0.3 ok
# if __name__ == '__main__':
#     image2transparent('./images/image_style/rixi','./images/transparent/rixi',rate=0.5)