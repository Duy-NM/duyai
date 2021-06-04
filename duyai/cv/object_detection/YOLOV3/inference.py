import cv2
import time
import numpy as np
import core.utils as utils
import tensorflow as tf
from core.yolov3 import YOLOv3, decode

import sys
sys.path.append('../')
from utils import model_utils 

model       = None

def image_infer(image, image_size=416, weights='~/.duyai/yolo/yolov3.weights', classes_file='~/.duyai/yolo/coco.txt'):
    pass

