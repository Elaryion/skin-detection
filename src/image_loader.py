import cv2
import torch

class ImageLoader:
    @staticmethod
    def load_image(image_path: str):

        try:
            
            image = cv2.imread(image_path)
            if image is None:
                raise FileNotFoundError(f"Image not found at {image_path}")
            
            # Convert the image from BGR to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Normalize and convert to PyTorch tensor
            image_tensor = torch.from_numpy(image).permute(2, 0, 1).float() / 255.0
            
            return image, image_tensor.unsqueeze(0)
        except Exception as e:
            raise RuntimeError(f"Failed to load and preprocess the image at {image_path}: {e}")
