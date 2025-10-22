import cv2

src = "netflix.jpg"
destination = 'zed.jpeg'
scale_percent = 150
image = cv2.imread(src, cv2.IMREAD_UNCHANGED)

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
output = cv2.resize(image, (width, height))
cv2.imwrite(destination, output)
cv2.waitKey(0)