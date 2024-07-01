'''
Code formally written by Alexander James Porter (Contact: AlexanderPorter1234@gmail.com) 20/02/2023
Code has been optimised for reading screenshots of final scoreboard in the game VALORANT
Lots of code is utilised from https://github.com/eihli/image-table-ocr#org67b1fc2
'''
import sys
import cv2
import numpy as np
import pytesseract
import subprocess
import math
import csv
import json
from PIL import Image,ImageFilter
from scoreboard_reader import functions as srf

#Setting up tesseract - only needs this if you have directly installed tesseract (I think).
pytesseract.pytesseract.tesseract_cmd = "tesseract"

#Reads in your file and crops out the table using find_tables
image_filename = input("Please input the name of your screenshot (default is screenshot.png):   ")
if image_filename == "":
    image_filename = "screenshot.png"
image = cv2.imread(image_filename, cv2.IMREAD_GRAYSCALE)
image_colored = cv2.imread(image_filename)
image, image_colored = srf.find_tables(image,image_colored)

# #Extracts each row of elements from the table
cell_images_rows,headshots_images_rows = srf.extract_cell_images_from_table(image,image_colored)

agents = srf.identify_agents(headshots_images_rows)


#Reads the extracted rows and converts them to a list of lists.
output = srf.read_table_rows(cell_images_rows)


srf.write_csv(output,agents, ",")
srf.write_json(output,agents)
    
print("Done. Output written to scoreboard.csv and scoreboard.json.")



