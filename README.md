# Improving Multiple Drosophilla Tracking with Convolutional Neural Networks
A computer vision project conducted in conjunction with Imperial's Gillestro Laboratory during my Bioinformatics MSc. The aim was to detect and track multiple fruit flies in footage from behavioural experiments. There had been prevous attempts by the lab to utilise the Viola-Jones object detection framework, but this lead to inconsistent detection that often underpredicted the number of flies. I improved this by employing two CNN frameworks - YOLO (Darknet) & Faster R-CNN (Detectron 2).

The web-report for this project can be found at: https://improving-object-tracking-using-deep-le.webflow.io/


## How to use this Repo: 
### Viola-Jones
The Scripts for the Viola Jones Object Detection method can be found in the "Haar" Directory. To utilise this, you will need the following dependencies: 
1) OpenCV
2) The Ethoscope Development Branch  https://github.com/gilestrolab/ethoscope

### CNN Methods
The Collab Notebooks for Faster R-CNN & YOLO can be found below:


These are entirely self contained and should run straight out of the box.

