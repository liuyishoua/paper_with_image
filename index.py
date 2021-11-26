import os
import zipfile
# from waitress import serve
from core_function import main
from flask import Flask,render_template
from flask import request, send_from_directory, send_file
from PyPDF2 import PdfFileWriter, PdfFileReader
# os.chdir('C:\\Users\\刘志远\\AnacondaProjects\\2022 project\\paper_with_image')

app = Flask(__name__, static_url_path='')
app.config['STYLE_INFO'] = './core_function/images/style_info.txt'
app.config['UPLOAD_STYLE_IMAGE'] = './core_function/images/image_style'
app.config['UPLOAD_STYLE_TRANSPARENT'] = './core_function/images/transparent'
app.config['UPLOAD_STYLE_PDF'] = './core_function/images/pdf'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['HANDLE_FOLDER'] = './handle_pdf'
app.config['STYLE_ROOT'] = 'core_function/images/pdf'

@app.route('/')
def index():
    return render_template('index.html')
#     data = request.args.get('button')

@app.route('/style/custom')
def custom():
    return render_template('style_custom.html')

@app.route('/upload/style_image',methods=['GET','POST'])
def upload_style():
    # request.get.arg yu request.form.getlist
    files = request.files.getlist('filename')
    chinese_name = request.form.get('chinese_name')
    simple_name = request.form.get('simple_name')
    transparent = request.form.get('transparent')
    float_transparent = float(transparent)
    write_or_not_flag = 0
    if not transparent:
        return '透明度没有值'
    if not chinese_name:
        return '风格中文名没有值'
    if not simple_name:
        return '简写名没有值'
    if float_transparent < 0 or float_transparent > 1:
        return '透明度范围为0-1，请按要求填写值'
    upload_folder_name = simple_name
    upload_folder_path = os.path.join(app.config['UPLOAD_STYLE_IMAGE'],upload_folder_name)
    
    if not os.path.exists(upload_folder_path):
        os.makedirs(upload_folder_path)
        write_or_not_flag = 1
    for file in files:
        filename = file.filename
        if os.path.splitext(filename)[1] != '.jpg' and os.path.splitext(filename)[1] != '.jpeg' and os.path.splitext(filename)[1] != '.png':
            return '上传存在非法图片，该系统仅支持jpg,jpeg与png格式'
        
    for file in files: 
        filename = file.filename
        file_path = os.path.join(upload_folder_path,filename)
        # if filename not in os.listdir(app.config['UPLOAD_FOLDER']):
        file.save(file_path)

    main.preprocess(app.config['UPLOAD_STYLE_IMAGE'],app.config['UPLOAD_STYLE_TRANSPARENT'],app.config['UPLOAD_STYLE_PDF'],float_transparent,upload_folder_name)    
    if write_or_not_flag:
        with open(app.config['STYLE_INFO'],'a') as file:
            file.write('\n'+simple_name+' '+chinese_name)
    return "风格图片上传成功"
    
@app.route('/style/file')
def file():
    return render_template('upload_file.html',style_list = get_style_list(app.config['STYLE_INFO']))

# 访问静态资源，需要自己设置
# 由于html url路径，只会进行flask进行路由。
# 故需要单独为需要下载的文件设置路由
@app.route('/handle_pdf/<path:filename>')
def send_js(filename):
    return send_from_directory(directory=os.path.join(app.config['HANDLE_FOLDER']),filename=filename)

# parameter file and style.
@app.route('/uploads/file', methods = ['GET','POST'])
def handle_file():
    print ('123')
    file = request.files['filename']
    filename = file.filename
    style_list = request.form.getlist('style_list')
    if file:
        if os.path.splitext(filename)[1] != '.pdf':
            return 'What you have upload is not pdf file, Please return and input the specify file'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        file.save(file_path)
        
        input_file = PdfFileReader(open(file_path, "rb"))
        output_file = main.handle_file(input_file,style_list,app.config['STYLE_ROOT'])
        output_file_path = os.path.join(app.config['HANDLE_FOLDER'],filename) 
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        with open(output_file_path, "wb") as outputStream:
            output_file.write(outputStream)
        return render_template('upload_file.html',filename='http://127.0.0.1:5000/handle_pdf/'+filename,style_list = get_style_list(app.config['STYLE_INFO']))
    return "hello"

@app.route('/style/file_folder')
def file_folder():
    return render_template('upload_folder.html',style_list = get_style_list(app.config['STYLE_INFO']))

# parameter file and style.
@app.route('/uploads/file_folder', methods = ['GET','POST'])
def handle_file_folder():
    # if many files, just add getlist is ok.
    files = request.files.getlist('filename')
    style_list = request.form.getlist('style_list')
    zip_name = 'style_pdf_files.zip'
    upload_folder_name = os.path.splitext(files[0].filename)[0]
    upload_folder_path = os.path.join(app.config['UPLOAD_FOLDER'],upload_folder_name)
    output_folder_path = os.path.join(app.config['HANDLE_FOLDER'],upload_folder_name)
    if os.path.exists(upload_folder_path):
        for file_path in os.listdir(upload_folder_path):
            os.remove(os.path.join(upload_folder_path,file_path))
    else:
        os.makedirs(upload_folder_path)
    if os.path.exists(output_folder_path):
        for file_path in os.listdir(output_folder_path):
            os.remove(os.path.join(output_folder_path,file_path))
    else:
        os.makedirs(output_folder_path)

    for file in files: 
        filename = file.filename
        file_path = os.path.join(upload_folder_path,filename)
        # if filename not in os.listdir(app.config['UPLOAD_FOLDER']):
        file.save(file_path)
        input_file = PdfFileReader(open(file_path, "rb"))
        output_file = main.handle_file(input_file,style_list,app.config['STYLE_ROOT'])
        # if filename not in os.listdir(app.config['HANDLE_FOLDER']):
        with open(os.path.join(output_folder_path,filename), "wb") as outputStream:
                output_file.write(outputStream)
    # delete the rest zip files which generate as the temp files
    for file_path in os.listdir('.'):
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.zip':
            os.remove(file_path)

    zip_files(output_folder_path,zip_name)
    return send_file(zip_name,
            mimetype = 'zip',
            attachment_filename= zip_name,
            as_attachment = True)

def zip_files(folder_path,zip_name):
    zipf = zipfile.ZipFile(zip_name,'w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk(folder_path):
        for file in files:
            zipf.write(os.path.join(folder_path,file))
    zipf.close() 

# 使用文件作为数据库，简单化。
def get_style_list(style_info_path):
    style_data = []
    with open(style_info_path,'r') as file:
        for line in file.readlines():
            data = line.split(' ')
            simple_name = data[0]
            chinese_name = data[-1].replace('\n','')
            style_data.append({'simple_name':simple_name,'chinese_name':chinese_name})
    return style_data

if __name__ == '__main__':
    app.run(port=5000)
    # serve(app, host='0.0.0.0', port=5000, threads=1) #WAITRESS!