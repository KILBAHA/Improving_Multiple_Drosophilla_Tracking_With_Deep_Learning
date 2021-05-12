import numpy as np
import cv2
import matplotlib.pyplot as plt
import re

def get_filename(path):
    file_start = max([i.start() for i in re.finditer(r'/',path)])+1 #get last slash ind
    file_end = max([i.start() for i in re.finditer(r'\.', path)]) # get last . ind
    return(path[file_start:file_end])

def track(cascade, test_vid, outfile, known_flies = 41, write_coords = True):
    #some input parameters
    show_window = False
    fly_cascade = cv2.CascadeClassifier(cascade) #potentially need to make coppy of xml and replace
    cap = cv2.VideoCapture(test_vid) #dl a test vid, replace filename
    
    outfile = 'Output/' + outfile
    
    #save to video
    ret, img = cap.read()
    x,y,c = img.shape
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    fileout = cv2.VideoWriter(outfile, fourcc, 25.0, (y,x))
    
    #process through

    fly_list = []
    fly_count = []
    while 1:
        ret, img = cap.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            flies = fly_cascade.detectMultiScale(img, scaleFactor= 1.1,
                                                      minNeighbors= 3, 
                                                      flags= 0,
                                                      minSize= (15, 15),
                                                      maxSize= (20, 20) )
            
            fly_list.append(flies) #stores all coords of flies
            fly_count.append(len(flies))
        
            for (x,y,w,h) in flies:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    
            #write frame to video
            fileout.write(img)
    
            #and show if asked
            if show_window:
                cv2.imshow('img',img)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
        else:
            break
    cap.release()
    fileout.release()
    cv2.destroyAllWindows()
    
    if write_coords == True:
        np.savez('Coords/Coords_' + get_filename(outfile), *fly_list[:])
    
    corrected_count = []
    
    
    for count in fly_count:
        corrected_count.append(count - known_flies)
        
    plt.figure()    
    plt.bar(range(0,len(corrected_count)),corrected_count)
    plt.ylim([-15,15])
    
    plt.xlabel('Frame')
    plt.ylabel('Count deviation')
    plt.title(cascade[:-4])
    
    abs_deviation = []
    for count in corrected_count:
        abs_deviation.append(abs(count))
        
    print('======' + cascade[:-4] + '=====')
    
    print('Absolute Deviation: ', sum(abs_deviation))
    
    print('Mean Fly count:', sum(fly_count)/len(fly_count))
    
#track('Enrichment.xml','/home/yusuf/Documents/VJ_Ethoscope/test.mp4','/home/yusuf/Documents/VJ_Ethoscope/output_combined.avi')

test_vid = 'test_vid.mp4'#path to video to be tested
#outfolder = 'Output/'#path to training folder 

track('Enrichment.xml', test_vid, 'Enrich_Test.avi')
track ('/home/yusuf/Documents/VJ_Ethoscope/cascade.xml',test_vid, 'CurationOld_Test.avi' )
track('Simple_Curation.xml', test_vid, 'Curation_Test.avi')

track ('Enrichment.xml','simple_vid.mp4', 'Enrichment_SimpleVid.avi', known_flies = 33)
track ('/home/yusuf/Documents/VJ_Ethoscope/cascade.xml','simple_vid.mp4', 'CurationOld_SimpleVid.avi', known_flies = 33)
track('Simple_Curation.xml', 'simple_vid.mp4', 'Curation_SimpleVid.avi', known_flies = 33)



