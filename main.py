#cisco
#jaspay
#xperi
#revanture
#onebanc

import cv2
import time
import os

def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    width = int(video.get(3))
    height = int(video.get(4))
    print("Video resolution is set to ", width, 'x', height)
    print("Help-- \n1. Press ESC key to exit")

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    datetime = time.strftime("recording %H-%M-%d-%m-%y")
    if not os.path.exists('footages'):
        os.makedirs('footages')
    output = cv2.VideoWriter(f'footages/{datetime}.mp4', fourcc, 20.0, (640, 480))
    
    while video.isOpened():
        check, frame = video.read()
        if check:
            frame = cv2.flip(frame, 1)
            t = time.ctime()
            cv2.rectangle(frame, (5, 5, 200, 20), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, "Camera 1", (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (5, 5, 5), 1)
            cv2.putText(frame, t, (240, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (5, 5, 5), 1)
            cv2.imshow('CCTV Camera', frame)
            output.write(frame)

            key = cv2.waitKey(1)
            if key == 27:  # ESC key
                print("Video footage saved")
                break
        else:
            print("Can't open camera, check configuration")
            break

    video.release()
    output.release()
    cv2.destroyAllWindows()

print("*" * 80 + "\n" + " " * 30 + "Welcome to CCTV software\n" + "*" * 80)
ask = int(input("Do you want to open camera \n1 Yes \n2 No\n>> "))
if ask == 1:
    cctv()
elif ask == 2:
    print("Bye Bye, Be Safe")
else:
    print("Invalid input")
