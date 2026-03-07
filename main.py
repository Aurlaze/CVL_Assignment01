import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('underexpose_photo.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

alpha = 1.3 
beta = 30    

enhanced = cv2.convertScaleAbs(img_rgb, alpha=alpha, beta=beta)

final_img = cv2.cvtColor(enhanced, cv2.COLOR_RGB2BGR)
cv2.imwrite('enhanced_result.jpg', final_img)