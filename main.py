import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
from PIL import Image
from PIL import ImageEnhance
import os

# print(os.listdir(os.getcwd()))
# IMG_2495.JPG
# image = "IMG_2495.JPG"
image = "test.png"
#
img = Image.open(image)
# #處理圖片
img = ImageEnhance.Brightness(img).enhance(2.0)  # 增加亮度

img = ImageEnhance.Sharpness(img).enhance(17.0)  # 銳利化

img = ImageEnhance.Contrast(img).enhance(4.0)  # 增加對比度

img = img.convert('L')  # 灰度化
#
# #顯示原圖,呼叫系統預設的圖片顯示器
# img.show()
#
texts = pyzbar.decode(img)
print('12323123'[0:3])
print(texts[0].data.decode('utf-8'))
# #輸出結果
# for text in texts:
#     tt = text.data.decode("utf-8")
#     print(tt)
