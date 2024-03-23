import cv2
import numpy as np
# Read the original and duplicate images
original = cv2.imread("first.jpg")
duplicate = cv2.imread("second.jpg")
# Check if both images have the same shape
if original.shape == duplicate.shape:
    print("The images have the same size")
    # Calculate the pixel-wise difference between the images
    difference = cv2.subtract(original, duplicate)
    # Split the difference image into its individual BGR channels
    b, g, r = cv2.split(difference)
    # Check if all channels have zero non-zero pixels
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("Images are duplicates")
else:
    print("Images are not duplicates")