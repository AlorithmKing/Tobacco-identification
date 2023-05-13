from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'


image = Image.open('thres.jpg')


content = pytesseract.image_to_string(image,lang='eng', config='--psm 6 --oem 3 -c '
                                                                'tessedit_char_whitelist'
                                                                '=0123456789') # 解析图片
print(content)