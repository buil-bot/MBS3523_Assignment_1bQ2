import cv2
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    frame1 = frame
    frame2 = cv2.flip(frame, 0)
    frame3 = cv2.flip(frame, 1)
    frame4 = cv2.flip(frame, -1)

    frame1 = cv2.resize(frame1, (0, 0), fx=.5, fy=.5)
    frame2 = cv2.resize(frame2, (0, 0), fx=.5, fy=.5)
    frame3 = cv2.resize(frame3, (0, 0), fx=.5, fy=.5)
    frame4 = cv2.resize(frame4, (0, 0), fx=.5, fy=.5)

    top_row = cv2.hconcat([frame3, frame1])
    sec_row = cv2.hconcat([frame4, frame2])

    mix = cv2.vconcat([top_row, sec_row])

    cv2.imshow("Result", mix)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cam.release()
cv2.destroyAllWindows()

