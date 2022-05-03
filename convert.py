import cv2
import os
from skimage import io

dir_path = r'E:\Deep-learning\fewshotlogodetection_round1_train_202204\train\images'
for image_name in os.listdir(dir_path):
    image_path = os.path.join(dir_path,image_name)
    image = io.imread(image_path)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGRA)
    cv2.imencode('.jpg',image)[1].tofile(image_path)