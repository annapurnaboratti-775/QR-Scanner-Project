import cv2

path = r"C:\Users\lalit\Desktop\QR_Project\qr_image.png"

print("Loading:", path)
image = cv2.imread(path)

if image is None:
    print("Image loaded: False")
    print("ERROR: Could not read file. Check the filename and location.")
    exit()

print("Image loaded: True")

detector = cv2.QRCodeDetector()
data, points, _ = detector.detectAndDecode(image)

if data:
    print("Decoded data:", data)
else:
    print("No QR data found!")

# Draw bounding box ONLY if points exist
if points is not None:
    points = points[0]  # reshape
    for i in range(4):
        pt1 = tuple(map(int, points[i]))
        pt2 = tuple(map(int, points[(i + 1) % 4]))
        cv2.line(image, pt1, pt2, (0, 255, 0), 3)

    cv2.imwrite("qr_detected.png", image)
    print("Saved: qr_detected.png")
else:
    print("No corner points found — skipping drawing.")
