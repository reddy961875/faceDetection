import cv2
import mediapipe as mp
import time



from main import cap, bboxC


class FaceDetector():
    def __init__(self,minDetection=0.5):
        self.minDetectionCon = self.minDetectionCon
        self.mpFaceDetection =mp.solutions.face_detection
        self.mpDraw =mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self,img,draw =True):
        imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        #print(self.results)
        bboxs =[]

        if self.results.detections:
           for id,detection in enumerate(self.sresults.detections):
            bboxC =detection.location_data.relative_bounding_box
            ih,iw,ic =img.shape
            bboxC = int(bboxC.xmin * iw),int(bboxC.ymin  *ih),\
                int(bboxC.width * iw),int(bboxC.height * ih)
            bboxs.append(([id,bboxs,detection.score]))
            img = self.fancyDraw((img,bboxs))

            cv2.rectangle(img,bboxC,(255,0,255),2)
        cv2.putText(img, f'Fps: {int(detection.score[0]*100)}%', (bboxC[0],bboxC[1]-20), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 2)

        return img,bboxs

    def fancyDraw(self,img,bbox,l=30,t=10,rt=1):
        x,y,w,h =bbox
        x1,y1, =x+w,y+h
        cv2.rectangle(img, bboxC, (255, 0, 255), rt)
        cv2.line(img,(x1,y),(x1+l,y),(255,0,255),t)
        cv2.line(img,(x1,y),(x1,y+l),(255,0,255),t)

        return img


def main():
        cap = cv2.VideoCapture("posevideo1.mp4")
        pTime = 0
        detector = FaceDetector()
        while True:
            succes ,img = cap.read()
        img,bboxs= detector.findFaces(img)
        print(bboxs)

        cTime =time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img,f'Fps: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
        cv2.imshow("Image,", img)
        cv2.waitKey(1)


if __name__ =="__main__":
    main()

