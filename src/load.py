import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import warnings
warnings.filterwarnings('ignore')

import torch
from pathlib import Path
from copy import deepcopy

from model import Model

# Define the path to the save image folder
save_path = "./results"
# Define the path to the model file
model_path = './models/fasterrcnn_resnet50_fpn_epoch699.pkl'

# Initialize the Model class
model_wrapper = Model(model_path)

# Access the loaded model and device
model = model_wrapper.model
device = model_wrapper.device

# Perform inference or other operations with `model` and `device`
print(f"Model loaded successfully on {device}.")
