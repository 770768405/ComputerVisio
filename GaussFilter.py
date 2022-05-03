import numpy as np
import cv2

def GaussF(img,var=1,size=3):
    h,w,c = img.shape
    padding = size // 2
    padding_img = np.zeros((h+2*padding,w+2*padding,c),dtype=np.float32)
    padding_img[padding:h+padding,padding:w+padding,:] = img.copy().astype(np.float32)
    gausskernel = np.zeros((size,size),dtype=np.float32)
    for i in range(-padding,padding+1):
        for j in range(-padding,padding+1):
            gausskernel[i,j] = np.exp(-(i**2+j**2)/(2*var**2))
    gausskernel /= 2*np.pi*var**2
    gausskernel /= gausskernel.sum()

    tmp = padding_img.copy()
    for y in range(h):
        for x in range(w):
            for ci in range(c):
                padding_img[y+padding,x+padding,ci] = np.sum(gausskernel*tmp[y:y+size,x:x+size,ci])
    return padding_img[padding:h+padding,padding:w+padding,:]

if __name__ == '__main__':
    img = cv2.imread(r'E:\Deep-learning\ComputerVisio\draw\4e355d3fbc82a57172ecf1800f19d86b.jpg')
    # cv2.imshow('1',img)
    img = GaussF(img)
    cv2.imwrite('1.jpg',img)

