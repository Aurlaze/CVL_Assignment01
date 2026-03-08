import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. LINEAR TRANSFORM (For Dark Images)
img_dark = cv2.imread('dark_image.jpg')
img_dark_rgb = cv2.cvtColor(img_dark, cv2.COLOR_BGR2RGB)

alpha = 1.3
beta = 30 
enhanced_linear = cv2.convertScaleAbs(img_dark_rgb, alpha=alpha, beta=beta)

# 2. POWER-LAW / GAMMA TRANSFORM (For Bright Images)
img_bright = cv2.imread('bright_image.jpg')
img_bright_rgb = cv2.cvtColor(img_bright, cv2.COLOR_BGR2RGB)

gamma = 2.5
c = 1.0

table = np.array([c * ((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
enhanced_gamma = cv2.LUT(img_bright_rgb, table)

cv2.imwrite('result_linear.jpg', cv2.cvtColor(enhanced_linear, cv2.COLOR_RGB2BGR))
cv2.imwrite('result_gamma.jpg', cv2.cvtColor(enhanced_gamma, cv2.COLOR_RGB2BGR))