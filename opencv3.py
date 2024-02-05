import cv2
# print(cv2.__version__)
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    canny = cv2.Canny(frame, 100, 100)
    cv2.imshow("original", frame)
    # cv2.imshow('frame', gray)
    cv2.imshow("blur", blur)
    cv2.imshow("canny", canny)
    cv2.imshow("hsv", hsv)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cam.release()
cv2.destroyAllWindows()
