import cv2 as cv

def detect_faces_and_eyes():
    """
    Detects faces and eyes in real-time using the webcam.
    Press 'q' to exit.
    """

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

    if face_cascade.empty() or eye_cascade.empty():
        print("❌ Error: Could not load Haar cascade files.")
        exit()

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Cannot access camera.")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("❌ Error: Failed to capture frame.")
            break

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(60, 60))

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        cv.imshow("Face and Eye Detection", img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    detect_faces_and_eyes()
