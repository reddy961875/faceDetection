import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("posevideo5.mp4")
pTime=0


#implementing facedetection module
mpFaceDetection =mp.solutions.face_detection   ##detect face
mpDraw =mp.solutions.drawing_utils             ## drawing lines
faceDetection = mpFaceDetection.FaceDetection()


while True:
    succes ,img = cap.read()
#decrese frame rate
    imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):

            #mpDraw.draw_detection(img,detection)
            print(id,detection)
            print(detection.score)
            print(detection.location_data.relative_bounding_box)
            bboxC =detection.location_data.relative_bounding_box
            ih,iw,ic =img.shape
            bboxC = int(bboxC.xmin * iw),int(bboxC.ymin  *ih),\
                int(bboxC.width * iw),int(bboxC.height * ih)
            center = (int(bboxC[0] + bboxC[2] / 2), int(bboxC[1] + bboxC[3] / 2))
            radius = int((bboxC[2] + bboxC[3]) / 4)
            cv2.circle(img, center, radius, (255, 0, 255), 2)




    cTime =time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'Fps: {int (fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
    cv2.imshow("Image,", img)

    cv2.waitKey(1)