import cv2
import numpy as np


def worker(img_dir: str) -> np.ndarray:
    image = cv2.imread(img_dir)
    tol = 5
    # Define the size of the block for color sampling
    sample_size = 5
    sample_color = np.mean(image[:sample_size, :sample_size, :], axis=(0, 1))
    # Define a tolerance value for color similarity (adjust as needed)
    tolerance = 40
    image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    # Create a mask for the pure color background using the sampled color and tolerance
    mask = np.all(np.abs(image[:, :, :3] - sample_color) <= tolerance, axis=2)
    # Use the mask to filter the pixels and change their alpha channel
    image_rgba[mask] = [0, 0, 0, 0]
    alpha_channel = image_rgba[:, :, 3]
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # im_bw = 255-cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(alpha_channel, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Initialize variables to store the coordinates of the bounding box
    x_min = float('inf')
    y_min = float('inf')
    x_max = 0
    y_max = 0
    if len(contours) > 0:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            x_min = min(x_min, x)
            y_min = min(y_min, y)
            x_max = max(x_max, x + w)
            y_max = max(y_max, y + h)
        cropped_image = image_rgba[y_min:y_max, x_min:x_max]
        return cropped_image
    else:
        return image_rgba