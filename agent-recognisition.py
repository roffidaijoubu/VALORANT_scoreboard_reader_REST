import cv2
import numpy as np
import os

# Load images and their filenames from a folder
def load_images_from_folder(folder):
    images = []
    agent_names = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            agent_names.append(os.path.splitext(filename)[0])  # Use the filename (without extension) as the agent name
    return images, agent_names

# Resize image to the given size
def resize_image(image, size=(50, 50)):
    return cv2.resize(image, size)

# Extract features using SIFT
def extract_features(image):
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors

# Match features between two images using Brute-Force and Ratio Test
def match_features(descriptors1, descriptors2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)
    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
    return good_matches

# Find the matching agent by comparing input image with reference images
def find_matching_agent(input_image_path, reference_images, agent_names):
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    input_image = resize_image(input_image, (50, 50))
    _, input_descriptors = extract_features(input_image)

    max_matches = 0
    matching_agent = None
    for i, ref_image in enumerate(reference_images):
        ref_image_gray = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)
        ref_image_gray = resize_image(ref_image_gray, (50, 50))
        _, ref_descriptors = extract_features(ref_image_gray)
        matches = match_features(input_descriptors, ref_descriptors)
        if len(matches) > max_matches:
            max_matches = len(matches)
            matching_agent = agent_names[i]
    
    return matching_agent

# Path to the folder containing reference images
reference_folder = './agent-images'
reference_images, agent_names = load_images_from_folder(reference_folder)

# Path to the input image to be matched
input_image_path = './agent.png'
matching_agent = find_matching_agent(input_image_path, reference_images, agent_names)
print(f'Matching agent: {matching_agent}')
