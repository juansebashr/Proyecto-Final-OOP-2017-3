import cv2

class douglas_peucker:
    def __init__(self,contours):
        # Contour aproximation, Douglas-Peucker algorithm
        epsilon = 0.01 * cv2.arcLength(contours, True)  # The 0.01 represents a percentage
        approx = cv2.approxPolyDP(contours, epsilon, True)
        self.approx=approx
