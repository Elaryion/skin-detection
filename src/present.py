import os
import matplotlib.pyplot as plt
import cv2
import acne_configs
from copy import deepcopy

class BoundingBoxPlotter:
    @staticmethod
    def plot_with_bbox(img, nms_boxes, nms_labels):

        try:
            linewidth = img.shape[0] // 500  # Adjust line width based on image size
            img_copy = deepcopy(img)
            
            # Create a matplotlib figure
            fig, ax = plt.subplots(1, 1, figsize=(24, 14))
            
            # Draw bounding boxes
            for box, _class in zip(nms_boxes, nms_labels):
                cv2.rectangle(img_copy, 
                              (box[0], box[1]), 
                              (box[2], box[3]),
                              acne_configs.ID_COLOR[_class], 
                              linewidth)
            
            # Display the image
            ax.imshow(img_copy)
            plt.show()
        except Exception as e:
            raise RuntimeError(f"Failed to plot image with bounding boxes: {e}")

    @staticmethod
    def save_image_with_bbox(img, nms_boxes, nms_labels, target_folder, output_filename):
        try:
            
             # Ensure valid image file extension (e.g., .jpg, .png)
            if not output_filename.endswith(('.jpg', '.png', '.jpeg', '.bmp')):
                raise ValueError("The output filename must have a valid image extension (.jpg, .png, .jpeg, .bmp).")

            linewidth = img.shape[0] // 500  # Adjust line width based on image size
            img_copy = deepcopy(img)

            # Draw bounding boxes on the image
            for box, _class in zip(nms_boxes, nms_labels):
                cv2.rectangle(img_copy, 
                              (box[0], box[1]), 
                              (box[2], box[3]),
                              acne_configs.ID_COLOR[_class], 
                              linewidth)
            
            # Ensure the target folder exists
            os.makedirs(target_folder, exist_ok=True)

            # Create the output path
            output_path = os.path.join(target_folder, output_filename)
            
            # Save the image
            cv2.imwrite(output_path, cv2.cvtColor(img_copy, cv2.COLOR_RGB2BGR))
            print(f"Image saved to {output_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to save image with bounding boxes: {e}")

    @staticmethod
    def encode_image_with_bbox(img, nms_boxes, nms_labels):
        try:
            linewidth = img.shape[0] // 500  # Adjust line width based on image size
            img_copy = deepcopy(img)

            # Draw bounding boxes on the image
            for box, _class in zip(nms_boxes, nms_labels):
                cv2.rectangle(img_copy, 
                              (box[0], box[1]), 
                              (box[2], box[3]),
                              acne_configs.ID_COLOR[_class], 
                              linewidth)

            return cv2.cvtColor(img_copy, cv2.COLOR_RGB2BGR)

        except Exception as e:
            raise RuntimeError(f"Failed to save image with bounding boxes: {e}")
