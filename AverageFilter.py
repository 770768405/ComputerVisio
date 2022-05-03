import numpy as np
import cv2

def average(img,size=3):
    h,w,c = img.shape
    padding = size // 2
    padding_img = np.zeros((h+2*padding,w+2*padding,c),dtype=np.float16)
    padding_img[padding:padding+h,padding:padding+w,:] = img.copy()

    temp = padding_img
    for y in range(h):
        for x in range(w):
            for ci in range(c):
                padding_img[y+padding,x+padding,ci] = np.mean(temp[y:y+size,x:x+size,ci])
    return padding_img[padding:padding+h,padding:padding+w,:]

if __name__ == '__main__':
    img = cv2.imread(r'C:\Users\ppc\Pictures\Camera Roll\image.jpg').astype(np.float16)
    img = average(img).astype(np.uint8)
    cv2.imwrite('2.jpg',img)