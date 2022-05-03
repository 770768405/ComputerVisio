import numpy as np
import cv2

def mid(img,size=3):
    h,w,c = img.shape
    padding = size // 2
    padding_img = np.zeros((h+2*padding,w+2*padding,c),dtype=np.float16)
    padding_img[padding:padding+h,padding:padding+w,:] = img.copy().astype(np.float16)

    temp = padding_img
    for y in range(h):
        for x in range(w):
            for ci in range(c):
                padding_img[padding+y,padding+x,ci] = np.median(temp[y:y+size,x:x+size,ci])
    return padding_img[padding:padding+h,padding:padding+w,:]

if __name__ == '__main__':
    img = cv2.imread(r'C:\Users\ppc\Pictures\Camera Roll\image.jpg')
    img = mid(img).astype(np.uint8)
    cv2.imwrite('3.jpg',img)