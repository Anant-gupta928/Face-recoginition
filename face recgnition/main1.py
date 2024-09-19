import cv2
import numpy as np

# img = cv2.imread("image.jpg")

#  "how to read image"  
# cv2.imshow("Output Image", img)

# "how to write image"
# cv2.imwrite("output.jpg", img)

# "get image information using opencv"
# print(img.shape)
# print("Height:", img.shape[0])
# print("widht:", img.shape[0])

# "image rotation using opencv"
# height ,widht = img.shape[: 2]
# Rotating =cv2.getRotationMatrix2D((widht / 2, height / 2), 90, .5)
# finalimg= cv2.warpAffine(img, Rotating,(widht, height))
# cv2.imshow("Rotating Image", finalimg)
# cv2.imshow("original", img)

# "image transpose using opencv"
# rotating = cv2.transpose(img)
# cv2.imshow("Transpose", rotating)
# cv2.imshow("Original", img)

# "capturing vedio using opencv"
# vedio = cv2.VideoCapture(0)

# while True:
#     check , frame = vedio.read()
#     cv2.imshow("frame", frame)
#     cv2.waitKey(0)

# # "how to crop image using open cv"
# img = cv2.imread("image.jpg")
# height, widht = img.shape[: 2]
# start_row, start_col = int(height * .15), int(widht* .15)
# end_row, end_col = int(height * .65), int(widht* .65)

# cropped = img[start_row: end_row, start_col: end_col]
# cv2.imshow("Cropped", cropped)
# cv2.imshow("Original", img)
# cv2.waitKey(0)

# # "how to blur image using opencv"
# img = cv2.imread("image.jpg")
# kernel = np.ones((7,7),np.float32) /49
# blurred = cv2.filter2D(img, -1, kernel)
# cv2.imshow("Blurred", blurred)
# cv2.waitKey(0)

# # "image praymid using opencv"
# img = cv2.imread("image.jpg")
# smaller = cv2.pyrDown(img)
# larger = cv2.pyrUp(img)

# cv2.imshow("original", img)
# cv2.imshow("larger", larger)
# cv2.imshow("smaller", smaller)
# cv2.waitKey(0)

# "Edg detection in opencv"
img = cv2.imread("image.jpg")
canny = cv2.Canny(img, 20, 170)
cv2.imshow("Canny", canny)
cv2.waitKey(0)



