import cv2
import time

video_filename = str(int(time.time()))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vw = cv2.VideoWriter("./video/" + video_filename + ".avi", fourcc, 20, (640, 480))

cv2.namedWindow("SONY IMAX179", cv2.WINDOW_NORMAL)
cv2.resizeWindow("SONY IMAX179", 640, 480)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while cap.isOpened():
	ret, frame = cap.read()
	if ret == True:
		cv2.imshow("SONY IMAX179", frame)
		vw.write(frame)
		key = cv2.waitKey(1)
		if (key & 0xFF == ord('q')):
			break
	else:
		break
		
cap.release()
vw.release()
cv2.destroyAllWindows()
