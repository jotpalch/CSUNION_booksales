import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

isbn = []
path = 'book.txt'
f = open(path, 'a')


def bc(img):
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        code = barcode.data.decode('utf-8')
        if(code not in isbn and code[0:3] == '978'):
            isbn.append(barcode.data.decode('utf-8'))
            print(code, file=f)
            print(code)
        if(code in isbn):
            print("check", code)


def detect():
    ipcam = 'http://admin:admin@Jotp.local:8081/'

    cap = cv2.VideoCapture(ipcam)

    while True:
        # 讀取當前幀
        ret, frame = cap.read()
        # 轉換為灰度圖是為了檢測到二維碼，如果是BGR圖很大概率是檢測不到二維碼
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bc(gray)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()
