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
