import cv2
import numpy as np
class identifier:
    def __init__(self, img, approx, pt):
        newImg = img
        if len(approx) == 4 or len(approx) == 6:
            c = "Cube"
            print(c)
            cv2.drawContours(newImg, approx, -1, (255, 0, 0), 3)
            cv2.putText(newImg, 'Cube', pt, cv2.FONT_HERSHEY_COMPLEX, 2, [0, 255, 255], 2)

            def rectangle_rotation(approx):
                rect = cv2.minAreaRect(approx)  # (center (x,y), (width, height), angle of rotation)
                return "Rotation: " + str(rect[2])

            rectangle_rotation(approx)
        elif len(approx) >= 8:
            c= "Cylinder"
            print(c)
            cv2.drawContours(newImg, approx, -1, (255, 0, 0), 3)
            cv2.putText(newImg, 'Cylinder', pt, cv2.FONT_HERSHEY_COMPLEX, 2, [0, 255, 255], 2)
        else:
            cv2.drawContours(newImg, approx, -1, (255, 0, 0), 3)
        self.c=c
        self.Rotation = rectangle_rotation(approx)
        self.ShowImage = cv2.imwrite("C:\\Users\\Liliana Reyes\\PycharmProjects\\OOP_Final_Project\\GUI\\newImg.jpg", newImg)
