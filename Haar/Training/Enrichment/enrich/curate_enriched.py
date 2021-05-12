import cv2

#put filenames into images list
images = []
with open('filenames.txt') as imnames:
    for line in imnames:
        images.append(line.strip())

fly_dict = {} #init dictionary of values


#itterate through all images, read to screen and accept key press to determine number of flies. 
#Store this in fly_dict
count = 0
for image in images: #remove slice to itterate through all vals
    count += 1    
    print(count, ' of ', len(images), ' --- ', count/len(images)* 100 , '%')
    ir = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    Winname = 'window'
    
    cv2.imshow(Winname, ir)
    cv2.moveWindow(Winname, 1720,1080) #moves to a sensible position on screen (centre)
    k = cv2.waitKey(0) & 0xFF
    
    if k == 27:
            break
    elif k == ord('0'):
        pass
    elif k == ord('1'):
        fly_dict[image] = 1
    elif k == ord('2'):
        fly_dict[image] = 2
    elif k == ord('3'):
        fly_dict[image] = 3
    elif k == ord('4'):
        fly_dict[image] = 4
    elif k == ord('5'):
        fly_dict[image] = 5
    elif k == ord('6'):
        fly_dict[image] = 6
    elif k == ord('7'):
        fly_dict[image] = 7
    elif k == ord('8'):
        fly_dict[image] = 8
    elif k == ord('9'):
        fly_dict[image] = 9
    
    cv2.destroyAllWindows()
    
#use fly_dict to write to file in .info format
with open('enriched.info', 'w') as outfile:
    for key, val in fly_dict.items():
        line = 'img/' + str(key) + '\t' + str(val)
        
        for i in range(0,val):
            line += '\t' + str(0) + '\t' + str(0) + '\t' + str(50) + '\t' + str(50)
        line += '\n'
        outfile.write(line)





