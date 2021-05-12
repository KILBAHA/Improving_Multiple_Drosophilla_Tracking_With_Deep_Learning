import numpy as np
import cv2
import pascal_voc_writer as pvw


def vid_to_img(vid, outfolder):
    vidcap = cv2.VideoCapture(vid)
    success, image = vidcap.read()
    count = 0
    
    while success:
        cv2.imwrite(outfolder+"/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        count+=1

outfolder = 'simple'
vid = 'simple_vid.mp4'

#vid_to_img(vid,outfolder) #uncomment if you need to generate images again

#for i in range(0,frms)


#writer = Writer('simple/')




coords = np.load('Coords_Curation_SimpleVid.npz') #index using coords['arr_x']


k_list = []
for k in coords.keys():
    k_list.append(k)

frm = 0
for k in k_list:
    fly_list = coords[k]
    path = outfolder + '/' + 'frame' + str(frm) + '.jpg'
    im = cv2.imread(path)
    h,w,c = im.shape
    writer = pvw.Writer(path, w,h) #may need to change w and h
    for fly in fly_list:
        writer.addObject('fly', fly[0], fly[1], fly[0]+fly[2], fly[1] + fly[3])
        #img = cv2.imread(path)
        #crp = cv2.imshow('cropped', img[fly[1]:fly[1]+fly[3],fly[0]:fly[0]+fly[2]])
        #cv2.waitKey(0)
    writer.save(path + '.xml')
    frm += 1
    