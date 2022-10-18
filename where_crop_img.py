# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:35:33 2021

@author: juanc
"""

import os
import matplotlib.pyplot as plt



data = {'x': [],'y':[] ,'w':[],'h':[]}

#directory="C:/Users/juanc/Documents/Semestre9/Unidad2/imagenes/yolo/thompson_vid1/anotaciones/"
#directory="C:/Users/juanc/yolo/Yolov5_DeepSort_Pytorch/yolov5/runs/detect/thompson_fullvid1/labels/"
directory="C:/Users/juanc/yolo/Yolov5_DeepSort_Pytorch/yolov5/runs/detect/redglobe_fullvid1/labels/"
os.chdir(directory) 

for entry in os.listdir():
    with open(entry, 'r') as f:
        for line in f:
            c, x, y, w, h = line.split(' ')
            data['x'].append(float(x)*1280)
            data['y'].append(float(y)*720)
            data['w'].append(float(w)*1280)
            data['h'].append(float(h)*720)    
'''
with open('0005.txt', 'r') as f:
    for line in f:
        c, x, y, w, h = line.split(' ')
        data['x'].append(float(x)*1920)
        data['y'].append(float(y)*1080)
        data['w'].append(float(w)*1920)
        data['h'].append(float(h)*1080) 
'''

max_x = int(max(data['x']))
min_x = int(min(data['x']))
max_y = int(max(data['y']))
min_y = int(min(data['y']))

print("max_x:{}\nmin_x:{}\nmax_y:{}\nmin_y:{}\n".format(max_x,min_x,max_y,min_y))
print("Cortar la imagen en Y entre {} y {}".format(min_y-10, max_y+10))        
#Save File
directory="C:/Users/juanc/Documents/Semestre9/Unidad2/resultados/nuevos_resultados/"

os.chdir(directory)  

#thompson 1920x1080 #redglobe 1280x720
plt.scatter(data['x'], data['y'])
plt.xlim(0,1280)
plt.ylim(0,720)
plt.gca().invert_yaxis()
plt.xlabel("Ancho (píxeles)", size = 16,)
plt.ylabel("Alto (píxeles)", size = 16)

plt.show()

       
'''
fig = plt.figure(figsize = [15,12])
fig.add_subplot(4,4,1)
plt.hist(data['x'], bins=20, color = 'green')
plt.grid()
plt.ylabel("X")
fig.add_subplot(4,4,5)
plt.scatter(data['x'], data['y'])
plt.gca().invert_yaxis()
plt.ylabel("Y")
fig.add_subplot(4,4,6)
plt.hist(data['y'], bins=20, color = 'green')
plt.grid()
fig.add_subplot(4,4,9)
plt.scatter(data['x'], data['h'])
plt.ylabel("Altura")
fig.add_subplot(4,4,10)
plt.scatter(data['y'], data['h'])
plt.gca().invert_xaxis()
fig.add_subplot(4,4,11)
plt.hist(data['h'], bins=20, color = 'green')
plt.grid()
fig.add_subplot(4,4,13)
plt.scatter(data['x'], data['w'])
plt.ylabel("Ancho")
plt.xlabel("X")
fig.add_subplot(4,4,14)
plt.gca().invert_xaxis()
plt.xlabel("Y")
plt.scatter(data['y'], data['w'])
fig.add_subplot(4,4,15)
plt.xlabel("Altura")
plt.scatter(data['h'], data['w'])
fig.add_subplot(4,4,16)
plt.xlabel("Ancho")
plt.hist(data['w'], bins=20, color = 'green')
plt.grid()
fig.tight_layout()
plt.savefig("yolo_redglobe_vid1.png")   
#plt.savefig("yolo_thompson_vid1.png")         
'''
