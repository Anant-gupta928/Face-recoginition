import cv2
face_cap = cv2.cas
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    cv2.imshow("vedio_live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break
    video_cap.release()