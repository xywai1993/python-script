# 此脚本的功能是把照片按照日期建文件夹分类，使用方式，把此脚本放在照片文件夹的同级目录，如下
    - test文件夹（里面是要分类的照片）
    - move.exe

dist里 move.exe 为打包后的文件

## 用到的库
 - exifread 读取照片的EXIF信息
 - shutil 文件高级操作库 python自带
 - os python自带
 - pyinstaller 打包工具， 把.py打包成exe 文件
