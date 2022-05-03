import numpy as np
import torch
import torch.nn as nn
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
class Conv2D:
    def __init__(self,in_channal,out_channal,kernal_size=3,pad=1,stride=1,same=None):
        self.in_channal = in_channal
        self.out_channal = out_channal
        if isinstance(kernal_size,int):
            self.kernal_size = (kernal_size,kernal_size)
        elif isinstance(kernal_size,tuple):
            self.kernal_size = kernal_size
        if isinstance(pad,int):
            self.pad = (pad,pad)
        elif isinstance(pad,tuple):
            self.pad = pad
        self.stride = stride
        self.same = same

        # initial the parameters of the kernel, do not initial them as zero
        self.weights = np.random.standard_normal([self.out_channal,self.in_channal, self.kernal_size[0], self.kernal_size[1]])
        self.bias = np.random.standard_normal([self.out_channal,1])

    def forward(self,x):
        b,c,h,w = x.shape
        if self.same:
            self.pad = (int(((h-1)*self.stride-h+self.kernal_size[0])/2),int(((w-1)*self.stride-w+self.kernal_size[1])/2))
            h_out = h
            w_out = w
        else:
            h_out = int((h + 2 * self.pad[0] - self.kernal_size[0]) / self.stride + 1)
            w_out = int((w + 2 * self.pad[1] - self.kernal_size[1]) / self.stride + 1)
        padding_img = np.zeros((b,c,h+2*self.pad[0],w+2*self.pad[1]),dtype=np.float32)
        padding_img[:,:,self.pad[0]:self.pad[0]+h,self.pad[1]:self.pad[1]+w] = x.copy().astype(np.float32)

        weights = self.weights.reshape([self.out_channal,-1])

        output = np.zeros((b,self.out_channal,h_out,w_out),dtype=np.float32)
        for i in range(b):
            x_i = padding_img[i]
            x_col = self.img2col(x_i)
            output[i] = np.reshape(np.dot(weights,x_col)+self.bias,output[0].shape)
        return output

    def img2col(self,padding_img):
        c,h,w = padding_img.shape
        img2col = []
        for y in range(0,h-self.kernal_size[0]+1,self.stride):
            for x in range(0,w-self.kernal_size[1]+1,self.stride):
                col = padding_img[:,y:y+self.kernal_size[0],x:x+self.kernal_size[1]].reshape([-1])
                img2col.append(col)
        x_col = np.array(img2col).swapaxes(0,1)
        return x_col

    def backward(self):
        pass

a = Conv2D(1,1,kernal_size=3,stride=1,pad=1)
b = torch.nn.Conv2d(1,1,kernel_size=3,stride=1,padding=1)
weight = np.random.random((1,1,3,3))
bais = np.random.random((1,1))
input = np.random.random((1,1,5,5))

a.weights = weight
a.bias = bais
b.weight = torch.nn.Parameter(torch.tensor(weight,dtype=torch.float32))
b.bias = torch.nn.Parameter(torch.tensor(bais.reshape([-1]),dtype=torch.float32))

a_output = a.forward(input)
b_output = b(torch.tensor(input,dtype=torch.float32))
# b_output.backward(torch.ones_like(b_output))
# print(b.weight)
# print(b.weight.grad)
print(a_output)
print(b_output)
