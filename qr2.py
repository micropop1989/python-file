import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("QR1.jpg"))
print("Decoded text is: ", val)