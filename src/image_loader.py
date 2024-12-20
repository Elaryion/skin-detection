import cv2
import torch
import numpy as np
import base64
import io
from PIL import Image

def load_image_base64(base64_data: str):
    try:
        img = np.array(Image.open(io.BytesIO(base64.b64decode(base64_data))))
        return preprocess(img)
    except Exception as e:
        raise RuntimeError(f"Failed to load or preprocess base64 image: {e}")

def load_image(image_path: str):
    try:
        return preprocess(cv2.imread(image_path))
    except Exception as e:
        raise RuntimeError(f"Failed to load or preprocess the image at {image_path}: {e}")

def preprocess(image):
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    # Normalize and convert to PyTorch tensor
    image_tensor = torch.from_numpy(image).permute(2, 0, 1).float() / 255.0
    
    return image, image_tensor.unsqueeze(0)

