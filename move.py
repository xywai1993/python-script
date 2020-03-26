# 此脚本的功能是把照片按照日期建文件夹文类，使用方式，把此脚本放在照片文件夹的同级目录，如下
# - 未分类文件夹
# - 此脚本


import exifread
import os
import shutil
folderdir = name = input("文件夹名称:")
noExif = 'noexif'
index=0

def move(file):
    global index
    filesrc = os.path.join(folderdir,file)
    f = open(filesrc, 'rb')
        # Return Exif tags
    tags = ''    
    try:
        tags = exifread.process_file(f)
       
    except KeyError:
        print(f'{file}解析不了跳过')
        f.close()
        return
    except:
        print(f'{file} 其他错误')
        f.close()
        return

    f.close()
    # 文件夹名称
    name = noExif
    if 'EXIF DateTimeDigitized' in tags:
        
        date =str(tags['EXIF DateTimeDigitized']).split(' ')[0].split(':') 
        name = '-'.join(date)


    # 文件夹路径    
    dirname = str(os.path.join(folderdir,name))   
    # 不存在目录则开始创建
    if os.path.exists(dirname) == False:
        os.mkdir(dirname)
    shutil.move(filesrc, os.path.join(dirname,file))
    print(f'移动{file}---->{dirname}')
    index=index+1           


files= os.listdir(folderdir)
for file in files:
    
    # if os.path.isdir(os.path.join(folderdir,file)):
    #     pass
    if os.path.isfile(os.path.join(folderdir,file)):
        move(file)
print(f'共处理图片{index}张')
end = input('按回车结束')
