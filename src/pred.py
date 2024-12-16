import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import warnings
warnings.filterwarnings('ignore')

import torch
from pathlib import Path
import numpy as np
from copy import deepcopy

import nms
from model import Model
from image_loader import ImageLoader
from present import BoundingBoxPlotter




# Define the path to the image file
image_path = "./images/lico2.jpg"

# Use the static method to load and preprocess the image
image, image_tensor = ImageLoader.load_image(image_path)

# Access the results
print("Image loaded successfully.")
print(f"Image shape: {image.shape}")
print(f"Image tensor shape: {image_tensor.shape}")


# Define the path to the model file
model_path = './models/fasterrcnn_resnet50_fpn_epoch699.pkl'

# Initialize the Model class
model_wrapper = Model(model_path)

# Access the loaded model and device
model = model_wrapper.model
device = model_wrapper.device

# Perform inference or other operations with `model` and `device`
print(f"Model loaded successfully on {device}.")


# Perform inference
image_tensor = image_tensor.to(device)
with torch.no_grad():
    preds = model([image_tensor.squeeze()])
    
# Extract predictions
preds = [{k: v.to('cpu') for k, v in t.items()} for t in preds]
pred_boxes = preds[0]['boxes']
pred_scores = preds[0]['scores']
pred_labels = preds[0]['labels']

# Apply NMS
keep_indices, count = nms.nms(pred_boxes, pred_scores, 0.3)
nms_boxes, nms_labels = pred_boxes[keep_indices[:count]], pred_labels[keep_indices[:count]]

# Plot the results
BoundingBoxPlotter.plot_with_bbox(image, nms_boxes.numpy().astype(np.int32), nms_labels.numpy())