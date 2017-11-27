# In this archive, it calls all the metods and construct the objetcs of the MV part

def vision():
    import csv
    import cv2
    import numpy as np
    from Machine_vision.Identifier import identifier
    from Machine_vision.Resizer import resizer
    from Machine_vision.Douglas_peucker import douglas_peucker

    # Data adquisition

    img = cv2.imread('C:\\Users\\Liliana Reyes\\PycharmProjects\\OOP_Final_Project\\Images\\Test_4.jpg')
    height, width = img.shape[:2]
    ResImg = resizer(img,height,width)
    img=ResImg.image

    # Pre-processing

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ##noise_removal = cv2.bilateralFilter(gray,9,75,75)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 11)
    canny_img = cv2.Canny(thresh, 250, 255)
    canny_img = cv2.convertScaleAbs(canny_img)

    # Processing
    kernel = np.ones((3, 3), np.uint8)
    dilated_img = cv2.dilate(canny_img, kernel, iterations=1)
    im2, contours, h = cv2.findContours(dilated_img, 1, 2)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    cnt = contours[0]  # contours

    # Recognition
    pt = (180, 3 * img.shape[0] // 4)
    for cnt in contours:
        D=douglas_peucker(cnt)
        approx = D.approx
        print("Number of corners: " + str(len(approx)))
        Result_image=identifier(img, approx,pt)

    with open('Result', 'w', newline='') as file:
        file.write("Number of corners: " + str(len(approx)))
        file.write('\n')
        file.write(Result_image.c)
        file.write('\n')
        file.write(Result_image.Rotation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
vision()