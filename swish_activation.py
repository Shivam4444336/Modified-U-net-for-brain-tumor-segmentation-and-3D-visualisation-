# -*- coding: utf-8 -*-
"""Swish_Activation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17B9FTS7GRU54eguh7KcEcnloZ7daQeN6
"""

from keras.backend import sigmoid
def swish(input):
  return input*sigmoid(input)