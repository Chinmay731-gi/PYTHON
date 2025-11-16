import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Failed to grab frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    _, thresholded = cv.threshold(gray, 40, 255, cv.THRESH_BINARY)

    contours, _ = cv.findContours(thresholded.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    convex_hulls = [cv.convexHull(contour) for contour in contours]

    frame_with_contours = cv.drawContours(frame.copy(), contours, -1, (0, 255, 0), 2)
    frame_with_convex_hulls = cv.drawContours(frame_with_contours.copy(), convex_hulls, -1, (255, 0, 0), 2)

    cv.imshow("Thresholded", thresholded)
    cv.imshow("Contours & Convex Hulls", frame_with_convex_hulls)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

