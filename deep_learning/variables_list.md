# Dataset Variables

## Input Variables

1. image_batch (Tensor) = batch class for the variables
2. image_count (int) = total number of variables
3. IMAGE_SIZE (const int) = number of pixels in image (256)
4. images (list) = list of path of images from the root folder
5. plant_class_names (list) = list of names of plants in the folder
6. plant_dataset (_BatchDataset) = batch of the dataset of the plant
7. potato_classes (list) = list of names of potato acc. to folder name
8. potatoes_dict (dict) = dict of label names as keys and list of paths as the values
9. potatoes_early_blight, potatoes_late_blight, potatoes_healthy = list of path of the potatoes in early blight
10. potatoes_label_dict (dict) = dict with keys as name of the disease and values as 0,1,2
11. X (list) = list of all images with pixel values
12. y (list) = list of the labels for respective X values index
13. X_scaled (list) = list of all the images that are scaled to 0 - 1 range
14. X_size_100 (list) = list of all the images that have 100 image size
