# -*- coding: utf-8 -*-
"""ResNet-Block.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K3aN8SieWbYfZGbgIQW47G2Mqha0iPqG
"""

from keras.layers import *
from tensorflow_addons.layers import GroupNormalization

def Resnet(input_,level,groups):
  x1 = Conv3D(filters=64*level,kernel_size=(3,3,3),padding='same')(input_)
  x1 = GroupNormalization(groups)(x1)
  x2 = Conv3D(filters=64*level,kernel_size=(3,3,3),padding='same')(input_)
  x2 = GroupNormalization(groups)(x2)
  x = Concatenate()([x1,x2])
  x = Activation(swish)(x)
  x1 = Conv3D(filters=64*level,kernel_size=(3,3,3),padding='same')(x)
  x1 = GroupNormalization(groups)(x1)
  x2 = Conv3D(filters=64*level,kernel_size=(3,3,3),padding='same')(x)
  x2 = GroupNormalization(groups)(x2)
  x = Concatenate()([x1,x2])
  x = Add()([input_,x])
  x = Activation(swish)(x)
  return x