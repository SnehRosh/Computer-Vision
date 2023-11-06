import cv2
import numpy as np
import os

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print("🫡 Video file not found\n{path_of_video}")
        return None
    video = cv2.VideoCapture(path_of_video)
    while True:
        status, frame=video.read()
        if not status: 
            print("🫡 Video could not be read!")
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(2)==ord('q'): #1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    videofile = r'C:\Users\Hp\Downloads\kgarten.mp4'
    load_video(videofile)