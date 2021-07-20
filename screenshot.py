import os
import cv2
import xlrd
import csv

frame_rate = 30

path = os.path.abspath(os.path.dirname(__file__))+'\\source' # 获取目录
for root, dirs, names in os.walk(path):
    for name in names:
        video_name = os.path.splitext(name)
        film_name = video_name[0]
        ext = video_name[1]  # 获取后缀名
        if ext == '.mp4':
            print('processing '+name)
            video_path = path+'\\'+film_name+'.mp4'
            print('Found video: ' + film_name)
            with open('./source/'+film_name+'.mp4.csv', newline='') as csvfile:
                temp_reader = csv.reader(csvfile, delimiter=',')
                data = list(temp_reader)
                print(data[2][0])
            
            try:
                os.makedirs(os.path.abspath(os.path.dirname(__file__))+'\\frames\\'+film_name)
                for row in data:
                    line = row[0]
                    temp = line.strip().split(':') # hr:min:sec:
                    # print(temp)
                    time= int(temp[0])*3600+int(temp[1])*60+int(temp[2])+int(temp[3])/frame_rate
                    # screenshot
                    cover_path = './frames/' + film_name + '/' + temp[0] + '-' + temp[1] + '-' + temp[2] + '-' + temp[3] + '.jpg'
                    print(cover_path)
                    vc = cv2.VideoCapture(video_path)  # obtain video
                    video_width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))  # video width
                    video_height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))  # video height
                    vc.set(cv2.CAP_PROP_POS_MSEC, time*1000)  # set time in ms
                    rval, frame = vc.read()  # read current frame，rval for checking whether suceed
                    if rval:
                        cv2.imwrite(cover_path, frame)  # save screenshot to cover_path
                    else:
                        print("Screenshot Failed")
            except Exception as e:
                print(f"Error: {e}")

input('Executed successfully, click any key to exit.')
            
# times = "time.txt"
# video_path = "target.mp4"
# cover_path = None
# frame_rate = 30

# try:
#     f = open(times)
#     lines = f.readlines()
#     for line in lines:
#         temp = line.strip().split(':') # hr:min:sec:
#         # print(temp)
#         time= int(temp[0])*3600+int(temp[1])*60+int(temp[2])+int(temp[3])/frame_rate
#         # screenshot
#         cover_path = './frames/' + temp[0] + '-' + temp[1] + '-' + temp[2] + '-' + temp[3] + '.jpg'
#         print(cover_path)
#         vc = cv2.VideoCapture(video_path)  # obtain video
#         video_width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))  # video width
#         video_height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))  # video height
#         vc.set(cv2.CAP_PROP_POS_MSEC, time*1000)  # set time in ms
#         rval, frame = vc.read()  # read current frame，rval for checking whether suceed
#         if rval:
#             cv2.imwrite(cover_path, frame)  # save screenshot to cover_path
#         else:
#             print("Screenshot Failed")
# except Exception as e:
#     print(f"Error: {e}")



# based on https://richardrenn.github.io/Python-OpenCV-Snapshot.html