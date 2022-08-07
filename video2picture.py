import cv2
import os

video_id = 1652251703
video_path = "./video/" + str(video_id) + ".avi"
picture_dir = "./picture/" + str(video_id) + "/"
os.mkdir(picture_dir)
print(video_path)

cap = cv2.VideoCapture(video_path)

count = 1

while True:
	ret, frame = cap.read()
	if ret == True:
		cv2.imwrite(picture_dir + str(count).zfill(5) + ".jpg", frame)
		print(count)
		count = count + 1
	else:
		print("Done.")
		break
	
cap.release()
	
