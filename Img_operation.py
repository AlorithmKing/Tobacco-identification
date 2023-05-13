import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'


def img_rotate(src, angel):
    h, w = src.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angel, 1.0)
    # 调整旋转后的图像长宽
    rotated_h = int((w * np.abs(M[0, 1]) + (h * np.abs(M[0, 0]))))
    rotated_w = int((h * np.abs(M[0, 1]) + (w * np.abs(M[0, 0]))))
    M[0, 2] += (rotated_w - w) // 2
    M[1, 2] += (rotated_h - h) // 2
    # 旋转图像
    rotated_img = cv2.warpAffine(src, M, (rotated_w, rotated_h))

    return rotated_img


def preprocess_image(image_path):
    image = cv2.imdecode(np.fromfile(file=image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    image = img_rotate(image, 90)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    df, thresh = cv2.threshold(blurred, 29, 255, cv2.THRESH_BINARY)

    return thresh

# Image.fromarray(self.pix).save('preprocessed_image.jpg')
