import os
from . import my_utils
from PIL import Image

def image2transparent(image_folder_path,output_folder_path,rate = 0.5):
    # accroding the size of image, to design a adptative method
    # actually 612,792
    x_paper = 620
    y_paper = 1100
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)
    # if image age is below 2 minites, we can get the image to transparent
    folder_filespath = my_utils.get_2minite_folder_filepath(image_folder_path)
    for iter,file_path in enumerate(folder_filespath):
        img = Image.open(file_path)
        x_s, y_s = img.size
        x_rate = x_paper/x_s
        y_rate = y_paper/y_s
        if x_rate >= y_rate:
            img = img.resize((int(x_s*x_rate),int(y_s*x_rate)))
        else:
            img = img.resize((int(x_s*y_rate),int(y_s*y_rate)))
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