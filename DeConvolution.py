import torch
import numpy as np

class Deconv2D:
    def __init__(self, in_channal, out_channal, kernal_size=3, pad=1, stride=1):
        self.in_channal = in_channal
        self.out_channal = out_channal
        if isinstance(kernal_size, int):
            self.kernal_size = (kernal_size, kernal_size)
        elif isinstance(kernal_size, tuple):
            self.kernal_size = kernal_size
        if isinstance(pad, int):
            self.pad = (self.kernal_size[0]-pad-1, self.kernal_size[1]-pad-1)
        elif isinstance(pad, tuple):
            self.pad = (self.kernal_size[0]-pad[0]-1, self.kernal_size[1]-pad[1]-1)
        self.stride = stride

        # initial the parameters of the kernel, do not initial them as zero
        self.weights = np.random.standard_normal(
            [self.out_channal, self.in_channal, self.kernal_size[0], self.kernal_size[1]])
        self.bias = np.random.standard_normal([self.out_channal, 1])

    def forward(self,x):
        b,c,h,w = x.shape
        h_ = h + (self.stride-1)*(h-1) + 2*self.pad[0]
        w_ = w + (self.stride-1)*(w-1) + 2*self.pad[1]
        padding_img = np.zeros((b,c,h_,w_),dtype=np.float32)
        padding_img[:,:,self.pad[0]:h_-self.pad[0]+1:self.stride,self.pad[1]:w_-self.pad[1]+1:self.stride] = x

        h_out = int((h_  - self.kernal_size[0]) / 1 + 1)
        w_out = int((w_  - self.kernal_size[1]) / 1 + 1)

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
        for y in range(0,h-self.kernal_size[0]+1,1):
            for x in range(0,w-self.kernal_size[1]+1,1):
                col = padding_img[:,y:y+self.kernal_size[0],x:x+self.kernal_size[1]].reshape([-1])
                img2col.append(col)
        x_col = np.array(img2col).swapaxes(0,1)
        return x_col

a = Deconv2D(in_channal=1,out_channal=1,kernal_size=3,pad=1,stride=2)
b = torch.nn.ConvTranspose2d(1,1,3,2,1)

weight = np.random.random((1,1,3,3)).astype(np.float32)
bais = np.random.random((1,1)).astype(np.float32)
a.weights = weight
a.bias = bais
b.weight = torch.nn.Parameter(torch.tensor(np.rot90(weight,2,(2,3)).copy(),dtype=torch.float32))
b.bias = torch.nn.Parameter(torch.tensor(bais.reshape([-1]),dtype=torch.float32))

input = np.random.random((1,1,3,3))
a_outout = a.forward(input)
b_output = b(torch.tensor(input,dtype=torch.float32))

print(a_outout)
print(b_output)