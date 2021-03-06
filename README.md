# Improving Multiple Drosophilla Tracking with Convolutional Neural Networks
A computer vision project conducted in conjunction with Imperial's Gillestro Laboratory during my Bioinformatics MSc. The aim was to detect and track multiple fruit flies in footage from behavioural experiments. There had been prevous attempts by the lab to utilise the Viola-Jones object detection framework, but this lead to inconsistent detection that often underpredicted the number of flies. I improved this by employing two CNN frameworks - YOLO (Darknet) & Faster R-CNN (PyTorch & Detectron 2).

The web-report for this project can be found at: https://improving-object-tracking-using-deep-le.webflow.io/


## How to use this Repo: 
### Viola-Jones
The Scripts for the Viola Jones Object Detection method can be found in the "Haar" Directory. To utilise this, you will need the following dependencies: 
1) OpenCV
2) The Ethoscope Development Branch from https://github.com/gilestrolab/ethoscope

### CNN Methods
The Collab Notebooks for Faster R-CNN & YOLO can be found below:

Faster R-CNN detection + Tracking:     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/KILBAHA/9dd146ec953412a0bddb76bf375568e5/detectron2_w_drosophila.ipynb)

YOLO detection:     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/KILBAHA/1fdf33d2859c98b1b22c889c22027818/drosophila_yolov4.ipynb)

DeepSORT with YOLO weights:    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/KILBAHA/ac8f70b5c4be61309850a4b69f4df322/deepsort.ipynb)

These are entirely self contained and run straight out of the box.

