# This class modify an image to make it manageable
import cv2
class resizer:
    def __init__(self,img,height,width):
        # Augment Size
        if height < 300 or width < 400:
            img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # Reduce Size
        elif height > 800 or width > 1000:
            r = 500.0 / img.shape[1]
            dim = (500, int(img.shape[0] * r))
            img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        else:
            img= img

        self.image = img