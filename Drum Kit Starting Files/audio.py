from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import cv2

clip=(VideoFileClip('C:/Users/Mohan/Videos/2026-02-21-18-06-01.mp4').subclipped(0,20).with_volume_scaled(0.7))

# txtclip=TextClip(font=None,text="Entry to castle",bg_color='green',color='white',font_size=90).with_duration(10).with_position('center')
#
# final_video=CompositeVideoClip(clip,txtclip)
# final_video.write_videofile("C:/Users/Mohan/Videos/2026-02-21-18-08-38.mp4", fps=30)

video=cv2.VideoCapture('C:/Users/Mohan/Videos/2026-02-21-18-06-01.mp4')

while True:
    ret,frame=video.read()
    if not ret:
        print("EOV")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video',frame)


video.release()
cv2.destroyAllWindows()
