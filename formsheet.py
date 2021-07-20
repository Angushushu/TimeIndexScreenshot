import xlsxwriter
import os
from PIL import Image

# obtain folder names
root = os.path.abspath(os.path.dirname(__file__))
source_path = root + '\\frames' # 获取目录
target_path = root + '\\sheets'
cell_height = 90
cell_width = 160
folders = []
for root, dirs, names in os.walk(source_path):
    for dir in dirs:
        # print('processing ' + dir)
        if dir.strip() != '':
            folders.append(dir)
# print(folders)
folders = {}.fromkeys(folders).keys()
# print(folders)
for dir in folders:
    print('processing ' + dir)
    # create folder
    try:
        workbook = xlsxwriter.Workbook(target_path+'\\'+dir+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 21.8)
        worksheet.set_column('B:B', 15)
        dir_path = source_path+'\\'+dir
        row_cnt = 1
        # go over all screenshots
        for root_, dirs_, names_ in os.walk(dir_path):
            for name in names_:
                image = Image.open(dir_path+'\\'+name)
                width, height = image.size
                # worksheet.set_column('A:A', ex_width)
                worksheet.set_row(row_cnt, 68)
                x_scale = cell_width/width
                y_scale = cell_height/height
                #insert image
                worksheet.insert_image(row_cnt, 0, dir_path+'\\'+name, {'x_scale': x_scale, 'y_scale': y_scale, 'positioning': 1})
                worksheet.write(row_cnt, 1, name.split('.')[0])
                row_cnt+=1
        workbook.close()
    except Exception as e:
        print(f"Error: {e}")

input('Executed successfully, click any key to exit.')