arr=[[7.562309, 11.58, 16.507017, 20.49, 25.23, 27.6, 36.63, 43.05, 46.86],
[4.62, 9.33, 13.41],
[3.75, 8.28, 12.84, 17.64, 21.18, 24.57, 27.66],
[1.44, 7.68, 12.24, 15.39, 19.74, 23.22, 26.19, 30.33],
[4.8, 7.2, 12.12, 16.02, 21.54, 25.62, 27.9, 32.25, 40.95, 49.95, 56.13, 61.56],
[4.47, 7.887049, 12.27, 15.75, 17.43, 23.1],
[3.63, 3.72, 10.53],
[6.45, 11.31, 17.64, 22.05, 26.55, 28.17, 33.06, 36.21, 38.16, 40.71, 51.09],
[1.389043, 5.58, 13.65, 16.32, 21.36, 25.89, 30.3, 35.22, 39.75, 43.38],
]
import sys,os
from itertools import chain
inaccurate=[]
for i in range(2,10):
    file_handler=open(os.path.join(sys.path[0],f'../media/rawtext/Media{i}.txt'),'r+',encoding='cp437',errors='ignore')
    times_length=len(arr[i])
    lines_length=len(file_handler.readlines())
    if times_length!=lines_length-1:
        inaccurate.append(i+1)
print(inaccurate)
    

