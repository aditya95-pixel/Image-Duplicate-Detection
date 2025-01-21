# Image Duplicate Detection using Python and OpenCV

## Image Loading
The script uses OpenCV's cv2.imread() function to load the original (first.jpg) and duplicate (second.jpg) images into memory.

## Dimension Check
The shape attribute of the images is compared to ensure they have the same size. If the dimensions don't match, the script concludes that the images are not duplicates.

## Pixel-Wise Difference Calculation
The cv2.subtract() function is used to compute the difference between the original and duplicate images, pixel by pixel. This function produces a new image where each pixel's value represents the absolute difference between corresponding pixels in the two input images.

## Channel Analysis
The difference image is split into its Blue, Green, and Red channels using cv2.split(). The cv2.countNonZero() function checks for non-zero pixel values in each channel.

## Result

If all channels contain only zero values, the script confirms that the images are duplicates.

Otherwise, the images are flagged as not being duplicates.
