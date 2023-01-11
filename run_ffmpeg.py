# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:37:24 2018

@author: RCISP
"""

import os

##################----------Set Parameters----------####################
video_input="J:/Saramad_bamdad/Data/data_low_light/meghdad_5min.mp4" # set video input
output_format=".jpg" # setting image format
start_time="00:00:00" # setting start time
Duration="0:05:00" # setting Duration time
Frame_per_second="2" # setting Frame Per Second

########################################################################
exe_code="ffmpeg.exe"
path, name= os.path.split(video_input)
name2=os.path.splitext(name)
dirname=name2[0] 

if not os.path.exists(path + '/' + dirname):
    os.mkdir(path + '/' + dirname)
else:
    print('Directory:' + dirname + ' is already exist')
   
output_file=path + '/' + dirname
os.system(exe_code + " -i " + video_input + " -ss " + start_time + " -t " + Duration + " -vf fps=" + Frame_per_second + " -q 0 " + output_file + "/img_%5d" + output_format)

