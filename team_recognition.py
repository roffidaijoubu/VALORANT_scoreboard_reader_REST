import cv2
import numpy as np
import logging
from agent_recognition import resize_image

def assign_team(input_image_path):
    input_image = cv2.imread(input_image_path)
    
    # Increase contrast and saturation
    lab = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to L-channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    
    # Merge the channels back
    lab = cv2.merge((l, a, b))
    input_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    # Increase saturation
    hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.add(s, 50)  # Increase saturation by 50
    hsv = cv2.merge((h, s, v))
    input_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    input_image = resize_image(input_image, (50, 50))
    
    # Extract the region of interest (ROI)
    roi = input_image[3:21, 2:4]  # y from 3 to 20, x from 3 to 6

    # debug roi
    # cv2.imwrite("roi.png", roi)
    
    # Calculate the mean color of the ROI
    mean_color = cv2.mean(roi)[:3]  # Get the mean BGR values
        
    # Debug hex_color
    # logging.info(mean_color)
    
    # Debug Unknown Team
    # if approximate_color(mean_color) == "unknown":
    #     import time
    #     timestamp = int(time.time())
    #     cv2.imwrite(f"unknown-{timestamp}.png", input_image)
    #     cv2.imwrite(f"unknown-roi-{timestamp}.png", roi)
    
    return approximate_color(mean_color)

def approximate_color(mean_color):
    # Approximate if the color is red or green
    if mean_color[2] > mean_color[1] and mean_color[2] > mean_color[0]:
        color_approximation = "attacker"
    elif mean_color[1] > mean_color[2] and mean_color[1] > mean_color[0]:
        color_approximation = "defender"
    else:
        color_approximation = "unknown"
    
    return color_approximation
