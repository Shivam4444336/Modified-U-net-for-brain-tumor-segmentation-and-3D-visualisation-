# -*- coding: utf-8 -*-
"""Modified U-Net.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11w7yeUzEksa6nJU3HgLAq2kRI4AlCaCp
"""

#Modified U net implementation
from keras.layers import *
from keras.engine import Input,Model
from tensorflow_addons.layers import GroupNormalization

l = []
x_in= Input(shape = (240,240,155,4))
x = ZeroPadding3D(padding = (0,0,(2,3)))(x_in)
x1 = Conv3D(filters = 64,kernel_size = (3,3,3),padding='same')(x)
x1 = GroupNormalization(8)(x1)
x2 = Conv3D(filters = 64,kernel_size = (3,3,3),padding='same')(x)
x2 = GroupNormalization(8)(x2)
x = Concatenate()([x1,x2])
x = Activation(swish)(x)
x = Resnet(x,1,8)
x = Resnet(x,1,8)
l.append(x)
x = Downsample(x,1,8)
print(x.shape)
x = Resnet(x,2,8)
x = Resnet(x,2,8)
x = Resnet(x,2,8)
l.append(x)
x = Downsample(x,2,16)
print(x.shape)
x = Resnet(x,4,16)
x = Resnet(x,4,16)
x = Resnet(x,4,16)
x = Resnet(x,4,16)
l.append(x)
x = Downsample(x,4,32)
print(x.shape)
x = Resnet(x,8,32)
x = Resnet(x,8,32)
x = Resnet(x,8,32)
x = Resnet(x,8,32)
x = Resnet(x,8,32)
x_conT = Conv3DTranspose(filters = x.shape[4],kernel_size=(4,4,4),strides=(2,2,2),padding='same')(x)
x_conT = Activation('relu')(x_conT)

x_up = UpSampling3D(size = (2,2,2))(x)
x = Add()([x_up,x_conT])
x = Conv3D(filters = l[-1].shape[4],kernel_size=(1,1,1))(x)
x = Add()([x,l[-1]])
x = Resnet(x,4,16)
x_conT = Conv3DTranspose(filters = x.shape[4],kernel_size=(4,4,4),strides=(2,2,2),padding='same')(x)
x_conT = Activation('relu')(x_conT)
x_up = UpSampling3D(size = (2,2,2))(x)
x = Add()([x_up,x_conT])
x = Conv3D(filters = l[-2].shape[4],kernel_size=(1,1,1))(x)
x = Add()([x,l[-2]])
x = Resnet(x,2,8)
x_conT = Conv3DTranspose(filters = x.shape[4],kernel_size=(4,4,4),strides=(2,2,2),padding='same')(x)
x_conT = Activation('relu')(x_conT)
x_up = UpSampling3D(size = (2,2,2))(x)
x = Add()([x_up,x_conT])
x = Conv3D(filters = l[-3].shape[4],kernel_size=(1,1,1))(x)
x = Add()([x,l[-3]])
x = Resnet(x,1,8)
x = Conv3D(filters = 1,kernel_size = (1,1,1))(x)
x = Cropping3D((0,0,(2,3)))(x)
x = Activation('sigmoid')(x)
modified_u_net  = keras.Model(inputs = x_in,outputs = x)
